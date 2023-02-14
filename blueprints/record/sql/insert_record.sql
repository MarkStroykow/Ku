UPDATE invite
SET book_id = (Select MAX(idbook) from book )
WHERE invdate = '$invdate' and id_patient = (select id from patient where name_patient = '$name_patient')