from enum import Enum

class ReportPeriod(Enum):
    DAY = "DAY"
    WEEK = "WEEK"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    YEAR = "YEAR"

class DistributorView(Enum):
    MANUFACTURING = "MANUFACTURING"
    SOURCING = "SOURCING"

class SellingProgram(Enum):
    RETAIL = "RETAIL"
    BUSINESS = "BUSINESS"
    FRESH = "FRESH"

class ReportOptions(Enum):
    reportPeriod = ReportPeriod
    distributorView = DistributorView
    sellingProgram = SellingProgram
