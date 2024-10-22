## Respostas às Perguntas sobre o Banco de Dados de Streaming de Música

**Com base no modelo entidade-relacionamento descrito anteriormente, as respostas para as 20 perguntas usando álgebra relacional são:**

**1. Liste o título de todas as músicas e suas durações.**

```sql
SELECT titulo, duracao FROM Musica;
```

**2. Encontre o nome de todos os artistas que têm mais de 5 músicas em seu repertório.**

```sql
SELECT nome FROM Artista 
WHERE id IN (SELECT artista_id FROM Musica GROUP BY artista_id HAVING COUNT(*) > 5);
```

**3. Quais são os títulos dos discos lançados após 2020?**

```sql
SELECT titulo FROM Disco WHERE data_lancamento > '2020-12-31';
```

**4. Liste os títulos das músicas e os nomes dos artistas que as interpretam, ordenados pelo título da música.**

```sql
SELECT m.titulo AS Musica, a.nome AS Artista
FROM Musica m
JOIN Artista a ON m.artista_id = a.id
ORDER BY m.titulo;
```

**5. Encontre os títulos das playlists que contém a música com o título 'Imagine'.**

```sql
SELECT p.titulo 
FROM Playlist p
JOIN Musica m ON FIND_IN_SET(m.id, p.musica_ids) 
WHERE m.titulo = 'Imagine';
```

**6. Liste os usuários que criaram playlists que contém músicas do disco 'Abbey Road'.**

```sql
SELECT DISTINCT u.nome
FROM Usuario u
JOIN Playlist p ON u.id = p.usuario_id
JOIN Musica m ON FIND_IN_SET(m.id, p.musicas_ids)
JOIN Disco d ON m.disco_id = d.id
WHERE d.titulo = 'Abbey Road';
```

**7. Qual é a duração média das músicas de um artista específico?**

```sql
SELECT AVG(duracao) FROM Musica WHERE artista_id = <id_do_artista>;
```

**8. Encontre todos os artistas que não têm músicas.**

```sql
SELECT nome FROM Artista 
WHERE id NOT IN (SELECT DISTINCT artista_id FROM Musica);
```

**9. Liste todos os discos que contém mais de 10 músicas.**

```sql
SELECT d.titulo 
FROM disco d
JOIN musica m ON FIND_IN_SET(m.id, d.musica_ids)
GROUP BY d.id
HAVING COUNT(DISTINCT m.id) > 10;;
```

**10. Quais são os nomes dos artistas que têm discos lançados antes de 2010 e que têm músicas na playlist 'Top 50'?**

```sql
SELECT DISTINCT a.nome
FROM Artista a
JOIN Disco d ON a.id = d.artista_id
JOIN Musica m ON FIND_IN_SET(m.id, d.musica_ids)
JOIN Playlist p ON FIND_IN_SET(m.id, p.musica_ids)
WHERE d.data_lancamento < '2010-01-01' AND p.titulo = 'Top 50';             
```

**11. Quais músicas são interpretadas por mais de um artista?**

```sql
SELECT titulo FROM Musica GROUP BY titulo HAVING COUNT(DISTINCT artista_id) > 1;
```

**12. Liste os títulos das músicas que aparecem em mais de uma playlist.**

```sql
SELECT m.titulo
FROM Musica m
JOIN Playlist p ON FIND_IN_SET(m.id, p.musica_ids)
GROUP BY m.id
HAVING COUNT(DISTINCT p.id) > 1;
```

**13. Encontre os nomes dos usuários que têm playlists que incluem a música 'Bohemian Rhapsody'.**

```sql
SELECT DISTINCT u.nome
FROM Usuario u
JOIN Playlist p ON u.id = p.usuario_id
JOIN Musica m ON FIND_IN_SET(m.id, p.musica_ids)
WHERE m.titulo = 'Bohemian Rhapsody';
```

**14. Qual é o título da música mais longa do disco 'Dark Side of the Moon'?**

```sql
SELECT m.titulo
FROM Musica m
JOIN Disco d ON m.disco_id = d.id
WHERE d.titulo = 'Dark Side of the Moon'
ORDER BY m.duracao DESC
LIMIT 1;
```

**15. Liste todos os discos lançados por um artista específico em um de terminado ano.**

```sql
SELECT d.titulo
FROM Disco d
JOIN Artista a ON d.artista_id = a.id
WHERE a.nome = 'Gary Murphy' AND YEAR(d.data_lancamento) = 1978;
```

**16. Quais são os nomes dos artistas que têm músicas em playlists criadas por um usuário específico?**

```sql
SELECT DISTINCT a.nome
FROM Artista a
JOIN Disco d ON a.id = d.artista_id
JOIN Musica m ON FIND_IN_SET(m.id, d.musica_ids)
JOIN Playlist p ON FIND_IN_SET(m.id, p.musica_ids)
JOIN Usuario u ON p.usuario_id = u.id
WHERE u.nome = 'Nome do Usuário';
```

**17. Encontre a lista de músicas que não estão em nenhuma playlist.**

```sql
SELECT m.titulo
FROM Musica m
WHERE NOT EXISTS (
    SELECT 1
    FROM Playlist p
    WHERE FIND_IN_SET(m.id, p.musica_ids)
);
```

**18. Liste os títulos das músicas e os nomes dos artistas que têm mais de 3 músicas em uma mesma playlist.**

```sql
SELECT m.titulo, a.nome
FROM Musica m
JOIN Disco d ON m.disco_id = d.id
JOIN Artista a ON d.artista_id = a.id
JOIN Playlist p ON FIND_IN_SET(m.id, p.musica_ids)
GROUP BY m.id, a.id
HAVING COUNT(DISTINCT p.id) > 3;
```

**19. Quais são os discos que contém músicas de artistas que têm pelo menos 2 discos lançados?**

```sql
SELECT DISTINCT d.titulo 
FROM Disco d 
JOIN Musica m ON d.id = m.disco_id 
JOIN Artista a ON m.artista_id = a.id 
WHERE a.id IN (SELECT DISTINCT artista_id FROM Disco GROUP BY artista_id HAVING COUNT(*) >= 2);
```

**20. Liste todos os usuários e suas playlists, mas apenas para playlists que contém pelo menos 5 músicas.**

```sql
SELECT u.nome AS usuario, p.titulo AS playlist
FROM Usuario u
JOIN Playlist p ON u.id = p.usuario_id
WHERE LENGTH(p.musica_ids) - LENGTH(REPLACE(p.musica_ids, ',', '')) + 1 >= 5;
```

