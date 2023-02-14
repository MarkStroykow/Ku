SELECT b.jalobi, b.diagnoz, b.naznach, i.invdate
FROM patient p, invite i, book b
Where p.id in (Select id from patient where name_patient = '$name_patient') and p.id = i.id_patient and i.book_id = b.idbook;