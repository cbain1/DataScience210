--1
SELECT COUNT(*) AS count FROM Participants WHERE diet="dip";

--2
SELECT topic, COUNT(title) FROM Talks GROUP BY topic;

--3
SELECT title FROM Talks WHERE sid is Null;

--4
SELECT Participants.pid, fname || ' ' || lname AS participantName, Talks.title, talks.tid, Sessions.room, Sessions.start AS SessionBegins, Sessions.stop AS SessionEnds,
	CASE WHEN Sessions.start=-1 THEN '7:40am til 8:00am' AS SetUp,
	CASE 
        WHEN talks.tid = Sessions.tid1 THEN Sessions.start 
        WHEN talks.tid = Sessions.tid2 THEN Sessions.start+1
        WHEN talks.tid = Sessions.tid3 THEN Sessions.start+2
    END AS TalkBegins, 
    CASE 
        WHEN talks.tid = Sessions.tid1 THEN Sessions.start+1
        WHEN talks.tid = Sessions.tid2 THEN Sessions.start+2
        WHEN talks.tid = Sessions.tid3 THEN Sessions.stop 
    END AS TalkEnds

FROM Participants 
INNER JOIN attendance ON attendance.pid = participants.pid
INNER JOIN talks ON talks.tid = attendance.tid
INNER JOIN sessions ON sessions.sid = talks.sid 
ORDER BY participants.pid;

--5 
CREATE VIEW AS schedule
SELECT Participants.pid, fname || ' ' || lname AS participantName, Talks.title, talks.tid, Sessions.room, Sessions.start AS SessionBegins, Sessions.stop AS SessionEnds,
    CASE 
        WHEN talks.tid = Sessions.tid1 THEN Sessions.start 
        WHEN talks.tid = Sessions.tid2 THEN Sessions.start+1
        WHEN talks.tid = Sessions.tid3 THEN Sessions.start+2
    END AS TalkBegins, 
    CASE 
        WHEN talks.tid = Sessions.tid1 THEN Sessions.start+1
        WHEN talks.tid = Sessions.tid2 THEN Sessions.start+2
        WHEN talks.tid = Sessions.tid3 THEN Sessions.stop 
    END AS TalkEnds
FROM Participants 
INNER JOIN attendance ON attendance.pid = participants.pid
INNER JOIN talks ON talks.tid = attendance.tid
INNER JOIN sessions ON sessions.sid = talks.sid 
ORDER BY participants.pid;

SELECT a.participantName
FROM
    schedule AS a
    INNER JOIN schedule AS b
        ON  a.pid = b.pid
WHERE                     
    b.talkbegins <= a.talkbegins AND a.tid<>b.tid
GROUP BY a.pid;
