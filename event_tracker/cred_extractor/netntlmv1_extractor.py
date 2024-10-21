import re

from event_tracker.cred_extractor import CredentialExtractorGenerator
from event_tracker.models import Credential, HashCatMode

netntlmv1_regex = re.compile(r'(?P<hash>(?P<account>.+)::(?P<system>.+):[a-f0-9]{48}:[a-f0-9]{48}:[a-f0-9]{16})')


class NetNTLMv1Extractor(CredentialExtractorGenerator):
    def cred_generator(self, input_text: str, default_system: str):
        for match in netntlmv1_regex.finditer(input_text):
            yield Credential(**match.groupdict(), purpose="Windows Login", hash_type=HashCatMode.NetNTLMv1)
