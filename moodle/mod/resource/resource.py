from datetime import datetime
from typing import List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class File:
    """File
    Args:
        filename (Optional[str]): File name.
        filepath (Optional[str]): File path.
        filesize (Optional[int]): File size.
        fileurl (Optional[str]): Downloadable file url.
        timemodified (Optional[int]): Time modified.
        mimetype (Optional[str]): File mime type.
        isexternalfile (Optional[int]): Whether is an external file.
        repositorytype (Optional[str]): The repository type for external files.
    """

    filename: Optional[str] = None
    filepath: Optional[str] = None
    filesize: Optional[int] = None
    fileurl: Optional[str] = None
    timemodified: Optional[int] = None
    mimetype: Optional[str] = None
    isexternalfile: Optional[int] = None
    repositorytype: Optional[str] = None


@dataclass
class Resource:
    """Resource
    Args:
        id (int): Module id
        coursemodule (int): Course module id
        course (int): Course id
        name (str): Page name
        intro (str): Summary
        introformat (int):  Default untuk "1" intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        introfiles (List[File]): Files in the introduction text
        contentfiles (List[File]): Files in the content
        tobemigrated (int): Whether this resource was migrated
        legacyfiles (int): Legacy files flag
        legacyfileslast (Optional[int]): Legacy files last control flag
        display (int): How to display the resource
        displayoptions (str): Display options (width, height)
        filterfiles (int): If filters should be applied to the resource content
        revision (int): Incremented when after each file changes, to avoid cache
        timemodified (datetime): Last time the resource was modified
        section (int): Course section id
        visible (int): Module visibility
        groupmode (int): Group mode
        groupingid (int): Grouping id
    """

    id: int
    coursemodule: int
    course: int
    name: str
    intro: str
    introformat: int
    tobemigrated: int
    legacyfiles: int
    display: int
    displayoptions: str
    filterfiles: int
    revision: int
    timemodified: datetime
    section: int
    visible: int
    groupmode: int
    groupingid: int
    introfiles: List[File] = field(factory=list)
    contentfiles: List[File] = field(factory=list)
    legacyfileslast: Optional[int] = None


@dataclass
class Resources(ResponsesFactory[Resource]):
    """List of Resource
    Args:
        resources (List[Resource]): List of Resource
        warnings (List[Warning]): List of Warning
    """

    resources: List[Resource] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Resource]:
        return self.resources
