from datetime import datetime
from typing import List, Optional, Union

from moodle import ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class CourseFormatOption:
    """Format Option
    Args:
        name (str): course format option name
        value (Union[str, int]): course format option value
    """

    name: str
    value: Union[str, int]


@dataclass
class CourseShortData:
    """Course short data
    Args:
        id (int): course id
        shortname (str): Course short name
    """

    id: int
    shortname: str


@dataclass
class CourseCustomField:
    """Custom Field
    Args:
        name (str): The name of the custom field
        shortname (str): The shortname of the custom field
        type (str): The type of the custom field - text, checkbox...
        value (Optional[str]): The value of the custom field
    """

    name: str
    shortname: str
    type: str
    value: Optional[str] = None


@dataclass
class Course:
    """Course
    Args:
        id (int): course id
        shortname (str): course short name
        categoryid (int): category id
        categorysortorder (Optional[int]): sort order into the category
        fullname (str): full name
        displayname (str): course display name
        idnumber (Optional[str]): id number
        summary (str): summary
        summaryformat (int): summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        format (str): course format: weeks, topics, social, site,..
        showgrades (Optional[int]): 1 if grades are shown, otherwise 0
        newsitems (Optional[int]): number of recent items appearing on the course page
        startdate (int): timestamp when the course start
        enddate (int): timestamp when the course end
        numsections (Optional[int]): (deprecated, use courseformatoptions) number of weeks/topics
        maxbytes (Optional[int]): largest size of file that can be uploaded into the course
        showreports (Optional[int]): are activity report shown (yes = 1, no =0)
        visible (Optional[int]): 1: available to student, 0:not available
        groupmode (Optional[int]): no group, separate, visible
        groupmodeforce (Optional[int]): 1: yes, 0: no
        defaultgroupingid (Optional[int]): default grouping id
        timecreated (Optional[datetime]): timestamp when the course have been created
        timemodified (Optional[datetime]): timestamp when the course have been modified
        enablecompletion (Optional[int]): Enabled, control via completion and activity settings. Disbaled, not shown in activity settings.
        completionnotify (Optional[int]): 1: yes 0: no
        lang (Optional[str]): forced course language
        forcetheme (Optional[str]): name of the force theme
        hiddensections (Optional[int]): (deprecated, use courseformatoptions) How the hidden sections in the course are displayed to students
        courseformatoptions (List[CourseFormatOption]): additional options for particular course format
        customfields (List[CourseCustomField]): Custom fields and associated values
    """

    id: int
    shortname: str
    categoryid: int
    fullname: str
    displayname: str
    summary: str
    summaryformat: int
    format: str
    startdate: int
    enddate: int
    showgrades: Optional[int] = None
    newsitems: Optional[int] = None
    maxbytes: Optional[int] = None
    showreports: Optional[int] = None
    visible: Optional[int] = None
    groupmode: Optional[int] = None
    groupmodeforce: Optional[int] = None
    defaultgroupingid: Optional[int] = None
    enablecompletion: Optional[int] = None
    completionnotify: Optional[int] = None
    lang: Optional[str] = None
    categorysortorder: Optional[int] = None
    idnumber: Optional[str] = None
    numsections: Optional[int] = None
    timecreated: Optional[datetime] = None
    timemodified: Optional[datetime] = None
    forcetheme: Optional[str] = None
    hiddensections: Optional[int] = None
    courseformatoptions: List[CourseFormatOption] = field(factory=list)
    customfields: List[CourseCustomField] = field(factory=list)

    @dataclass
    class ToCheck:
        """Course To Check arg
        Args:
            contextlevel (str): The context level for the file location. Only module supported right now.
            id (int): Context instance id
            since (datetime): Check updates since this time stamp
        """

        contextlevel: str
        id: int
        since: datetime


@dataclass
class CourseByField(ResponsesFactory):
    """Get Course By Field
    Args:
        courses (List[Course]): Course
        warnings (List[Warning]): list of warnings
    """

    courses: List[Course] = field(factory=list)
    warnings: List[Warning] = field(factory=list)

    @property
    def items(self) -> List[Course]:
        return self.courses


@dataclass
class SearchResult(ResponsesFactory[Course]):
    """Search Result
    Args:
        total (int): total course count
        courses (List[Course]): course
        warnings (List[Warning]): list of warning
    """

    total: int
    courses: List[Course] = field(factory=list)
    warnings: List[Warning] = field(factory=list)

    @property
    def items(self) -> List[Course]:
        return self.courses


@dataclass
class CourseBTC:
    """Course By Time Classification
    Args:
        id (int): id
        fullname (str): fullname
        shortname (str): shortname
        idnumber (str): idnumber
        summary (str): summary
        summaryformat (int): summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        startdate (int): startdate
        enddate (int): enddate
        visible (int): visible
        fullnamedisplay (str): fullnamedisplay
        viewurl (str): viewurl
        courseimage (str): courseimage
        progress (Optional[int]): progress
        hasprogress (int): hasprogress
        isfavourite (int): isfavourite
        hidden (int): hidden
        timeaccess (Optional[int]): timeaccess
        showshortname (int): showshortname
        coursecategory (str): coursecategory
    """

    id: int
    fullname: str
    shortname: str
    idnumber: str
    summary: str
    summaryformat: int
    startdate: int
    enddate: int
    visible: int
    fullnamedisplay: str
    viewurl: str
    courseimage: str
    hasprogress: int
    isfavourite: int
    hidden: int
    showshortname: int
    coursecategory: str
    progress: Optional[int] = None
    timeaccess: Optional[int] = None


@dataclass
class CoursesBTC(ResponsesFactory[CourseBTC]):
    nextoffset: int
    courses: List[CourseBTC] = field(factory=list)

    @property
    def items(self) -> List[CourseBTC]:
        return self.courses


@dataclass
class CourseTU:
    """Course To Update
    Args:
        id (int): ID of the course
        fullname (Optional[str]):  full name
        shortname (Optional[str]):  course short name
        categoryid (Optional[int]):  category id
        idnumber (Optional[str]):  id number
        summary (Optional[str]):  summary
        summaryformat (Optional[int]):  summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        format (Optional[str]):  course format: weeks, topics, social, site,..
        showgrades (Optional[int]):  1 if grades are shown, otherwise 0
        newsitems (Optional[int]):  number of recent items appearing on the course page
        startdate (Optional[int]):  timestamp when the course start
        enddate (Optional[int]):  timestamp when the course end
        numsections (Optional[int]):  (deprecated, use courseformatoptions) number of weeks/topics
        maxbytes (Optional[int]):  largest size of file that can be uploaded into the course
        showreports (Optional[int]):  are activity report shown (yes = 1, no =0)
        visible (Optional[int]):  1: available to student, 0:not available
        hiddensections (Optional[int]):  (deprecated, use courseformatoptions) How the hidden sections in the course are displayed to students
        groupmode (Optional[int]):  no group, separate, visible
        groupmodeforce (Optional[int]):  1: yes, 0: no
        defaultgroupingid (Optional[int]):  default grouping id
        enablecompletion (Optional[int]):  Enabled, control via completion and activity settings. Disabled, not shown in activity settings.
        completionnotify (Optional[int]):  1: yes 0: no
        lang (Optional[str]): forced course language
        forcetheme (Optional[str]): name of the force theme
        courseformatoptions (Optional[List[CourseFormatOption]]): additional options for particular course format
        customfields (Optional[List[CourseCustomField]]): Custom fields
    """

    id: int
    fullname: Optional[str] = None
    shortname: Optional[str] = None
    categoryid: Optional[int] = None
    idnumber: Optional[str] = None
    summary: Optional[str] = None
    summaryformat: Optional[int] = None
    format: Optional[str] = None
    showgrades: Optional[int] = None
    newsitems: Optional[int] = None
    startdate: Optional[int] = None
    enddate: Optional[int] = None
    numsections: Optional[int] = None
    maxbytes: Optional[int] = None
    showreports: Optional[int] = None
    visible: Optional[int] = None
    hiddensections: Optional[int] = None
    groupmode: Optional[int] = None
    groupmodeforce: Optional[int] = None
    defaultgroupingid: Optional[int] = None
    enablecompletion: Optional[int] = None
    completionnotify: Optional[int] = None
    lang: Optional[str] = None
    forcetheme: Optional[str] = None
    courseformatoptions: Optional[List[CourseFormatOption]] = None
    customfields: Optional[List[CourseCustomField]] = None
