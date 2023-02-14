SELECT i.invdate, p.name_patient
FROM invite i, patient p
Where i.id_rasp in (select idrasp from rasp where docsid = (select id from doc where name_doc = '$name_doc')) and i.id_patient = p.id;