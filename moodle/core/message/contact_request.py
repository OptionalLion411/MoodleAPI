from typing import List, Optional

from moodle import MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class ContactRequestRecord:
    """Request Record
    Constructor arguments:
        id (int): Message id
        userid (int): User from id
        requesteduserid (int): User to id
        timecreated (int): Time created
    """

    id: int
    userid: int
    requesteduserid: int
    timecreated: int


@dataclass
class ContactRequest:
    """Contact Request
    Constructor arguments:
        request (Optional[ContactRequestRecord]): request record
        warnings (List[Warning]): list of warnings
    """

    request: Optional[ContactRequestRecord] = None
    warnings: List[MoodleWarning] = field(factory=list)
