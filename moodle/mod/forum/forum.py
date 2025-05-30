from typing import List, Optional

from moodle import MoodleObject
from moodle.attr import dataclass, field


@dataclass
class ForumFile:
    """File in Forum
    Constructor arguments:
    params: filename (Optional[str]): File name.
    params: filepath (Optional[str]): File path.
    params: filesize (Optional[int]): File size.
    params: fileurl (Optional[str]): Downloadable file url.
    params: timemodified (Optional[int]): Time modified.
    params: mimetype (Optional[str]): File mime type.
    params: isexternalfile (Optional[int]): Whether is an external file.
    params: repositorytype (Optional[str]): The repository type for external files.
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
class Forum(MoodleObject):
    """Forum
    Constructor arguments:
    params: id (int): Forum id
    params: course (int): Course id
    params: type (str): The forum type
    params: name (str): Forum name
    params: intro (str): The forum intro
    params: introformat (int): intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    params: duedate (Optional[int]): duedate for the user
    params: cutoffdate (Optional[int]): cutoffdate for the user
    params: assessed (int): Aggregate type
    params: assesstimestart (int): Assess start time
    params: assesstimefinish (int): Assess finish time
    params: scale (int): Scale
    params: maxbytes (int): Maximum attachment size
    params: maxattachments (int): Maximum number of attachments
    params: forcesubscribe (int): Force users to subscribe
    params: trackingtype (int): Subscription mode
    params: rsstype (int): RSS feed for this activity
    params: rssarticles (int): Number of RSS recent articles
    params: timemodified (int): Time modified
    params: warnafter (int): Post threshold for warning
    params: blockafter (int): Post threshold for blocking
    params: blockperiod (int): Time period for blocking
    params: completiondiscussions (int): Student must create discussions
    params: completionreplies (int): Student must post replies
    params: completionposts (int): Student must post discussions or replies
    params: cmid (int): Course module id
    params: numdiscussions (Optional[int]): Number of discussions in the forum
    params: cancreatediscussions (Optional[int]): If the user can create discussions
    params: lockdiscussionafter (Optional[int]): After what period a discussion is locked
    params: istracked (Optional[int]): If the user is tracking the forum
    params: unreadpostscount (Optional[int]): The number of unread posts for tracked forums
    """

    id: int
    course: int
    type: str
    name: str
    intro: str
    introformat: int
    assessed: int
    assesstimestart: int
    assesstimefinish: int
    scale: int
    maxbytes: int
    maxattachments: int
    forcesubscribe: int
    trackingtype: int
    rsstype: int
    rssarticles: int
    timemodified: int
    warnafter: int
    blockafter: int
    blockperiod: int
    completiondiscussions: int
    completionreplies: int
    completionposts: int
    cmid: int
    duedate: Optional[int] = None
    cutoffdate: Optional[int] = None
    numdiscussions: Optional[int] = None
    cancreatediscussions: Optional[int] = None
    lockdiscussionafter: Optional[int] = None
    istracked: Optional[int] = None
    unreadpostscount: Optional[int] = None
    introfiles: List[ForumFile] = field(factory=list)

    def __str__(self) -> str:
        return self.name
