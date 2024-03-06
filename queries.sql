SELECT users.username,
       users.id,
       profiles_1.first_name,
       profiles_1.last_name,
       profiles_1.id AS id_1,
       profiles_1.user_id
FROM users
         LEFT OUTER JOIN profiles AS profiles_1
             ON users.id = profiles_1.user_id
ORDER BY users.id;
