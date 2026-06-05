"""src/streaming/data_validation/data_contract_dawson.py.

Dawson-specific data contract module.

This module re-exports the current project data contract so
`kafka_consumer_dawson.py` can import a Dawson-named contract module.
"""

from streaming.data_validation.data_contract_case import (  # noqa: F401
    ALLOWED_CURRENCY_CODES,
    ALLOWED_DEVICE_TYPES,
    ALLOWED_PAYMENT_METHODS,
    ALLOWED_REFERRAL_SOURCES,
    CONSUMED_FIELDNAMES,
    CURRENCIES_REQUIRED_FIELDS,
    DISCOUNT_CODES_REQUIRED_FIELDS,
    PRODUCTS_REQUIRED_FIELDS,
    REGIONS_REQUIRED_FIELDS,
    REJECTED_SALES_FIELDNAMES,
    SALES_OPTIONAL_FIELDS,
    SALES_REQUIRED_FIELDS,
    VALID_SALES_FIELDNAMES,
    keep_sales_fields,
    validate_boolean_text,
    validate_datetime,
    validate_positive_integer,
    validate_required_fields,
    validate_sale_record,
)
