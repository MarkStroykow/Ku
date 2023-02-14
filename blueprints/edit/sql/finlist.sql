SELECT  p.name_patient, i.idin, i.invdate
FROM invite i, doc d, rasp r, patient p
where i.id_rasp = r.idrasp and r.docsid = d.id and i.id_patient = p.id and d.name_doc = '$name_doc';