import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from django.db import transaction
from django.forms import model_to_dict

from event_tracker.cred_extractor.askcreds_extractor import AskCredsExtractor
from event_tracker.cred_extractor.asreproast_extractor import PlainASREPRoastExtractor
from event_tracker.cred_extractor.browser_extractor import BrowserExtractor
from event_tracker.cred_extractor.credphisher_extractor import CredPhisherExtractor
from event_tracker.cred_extractor.domaincachedcredentials2_extractor import DCC2Extractor
from event_tracker.cred_extractor.kerberoast_extractor import PlainKerberoastExtractor
from event_tracker.cred_extractor.netntlmv1_extractor import NetNTLMv1Extractor
from event_tracker.cred_extractor.netntlmv2_extractor import NetNTLMv2Extractor
from event_tracker.cred_extractor.outflankkerberoast_extractor import OutflankKerberoastExtractor
from event_tracker.cred_extractor.rubeus_extractor import RubeusU2UExtractor, RubeusKerberoastExtractor, \
    RubeusASREPRoastExtractor
from event_tracker.cred_extractor.seatbelt_extractor import CredEnumExtractor
from event_tracker.cred_extractor.secretsdump_extractor import SecretsDumpDCSyncExtractor
from event_tracker.cred_extractor.snaffler_extractor import SnafflerExtractor
from event_tracker.cred_extractor.sprayad_extractor import SprayADExtractor
from event_tracker.models import Credential

executor = ThreadPoolExecutor()

extractor_classes = [SnafflerExtractor, BrowserExtractor, NetNTLMv1Extractor, NetNTLMv2Extractor,
                     AskCredsExtractor, CredPhisherExtractor, DCC2Extractor, SprayADExtractor, CredEnumExtractor,
                     OutflankKerberoastExtractor, RubeusU2UExtractor, RubeusKerberoastExtractor,
                     RubeusASREPRoastExtractor,
                     PlainKerberoastExtractor, PlainASREPRoastExtractor, SecretsDumpDCSyncExtractor]


@transaction.atomic
def extract_and_save(input_text: str, default_system: str):
    credentials = extract(input_text, default_system)

    creds_to_add_in_bulk = []
    for cred in credentials:
        print(f"{cred.account}@{cred.system} : {cred.secret} from {cred.source}")
        if cred.secret:
            # post-save action should be called, as we have a secret
            Credential.objects.get_or_create(**model_to_dict(cred))
        else:
            creds_to_add_in_bulk.append(cred)

    Credential.objects.bulk_create(creds_to_add_in_bulk, ignore_conflicts=True,
                                   unique_fields=["hash", "hash_type", "account", "system"])


def extract(input_text: str, default_system: str) -> [Credential]:
    credentials = []
    functions = [subclass().extract for subclass in extractor_classes]
    futures = []
    for function in functions:
        futures.append(executor.submit(function, input_text, default_system))
    for future in concurrent.futures.as_completed(futures):
        credentials += future.result()
    return credentials
