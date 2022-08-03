from typing import Any, Optional, Sequence

from django.apps.config import AppConfig
from django.core.checks.messages import CheckMessage, Error, Warning

SECRET_KEY_MIN_LENGTH: int
SECRET_KEY_MIN_UNIQUE_CHARACTERS: int
W001: Warning
W002: Warning
W004: Warning
W005: Warning
W006: Warning
W007: Warning
W008: Warning
W009: Warning
W018: Warning
W019: Warning
W020: Warning
W021: Warning
W022: Warning
E023: Error
E100: Error

def check_security_middleware(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_xframe_options_middleware(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_sts(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_sts_include_subdomains(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_sts_preload(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_content_type_nosniff(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_ssl_redirect(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_secret_key(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_debug(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_xframe_deny(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_allowed_hosts(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Warning]: ...
def check_referrer_policy(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[CheckMessage]: ...
def check_default_hashing_algorithm(app_configs: Optional[Sequence[AppConfig]], **kwargs: Any) -> Sequence[Error]: ...
