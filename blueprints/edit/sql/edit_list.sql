SELECT  r.numweek, d.name_doc
FROM rasp r, doc d
where r.docsid = d.id and r.numweek = '$week'