# Cleaning up imported data

Several PosgreSQL queries were used to cleanup repetitive data, since the relational model, while valuable for this approach, created a need for some normalizing steps.

### Finding duplicate item rows

```
SELECT
    entityid,
    event,
    COUNT( entityid )
FROM
    pio_event_1
WHERE
    Event='$set'
GROUP BY
    entityid,
    targetentityid,
    event,
    entitytype
HAVING
    COUNT( entityid )> 1
ORDER BY
    entityid,
    targetentityid,
    event;
```

### Delete duplicate item rows

```
DELETE FROM pio_event_2 
WHERE id IN
    (SELECT id
    FROM 
        (SELECT id,
         ROW_NUMBER() OVER( PARTITION BY entityid,
         event
        ORDER BY id ) AS row_num
        FROM pio_event_2 WHERE event='$set') t
        WHERE t.row_num > 1 );
```



### DUPLICATE VIEWS: IDENTIFY

```
SELECT
    targetentityid,
    event,
    COUNT( targetentityid )
FROM
    pio_event_2
WHERE
    Event='view'
GROUP BY
    targetentityid,
    entityid,
    event,
    entitytype
HAVING
    COUNT( targetentityid )> 1
ORDER BY
    targetentityid,
    entityid,
    event;
```


### DE-DUPLICATE VIEWS BY SAME USER

```
DELETE FROM pio_event_1 
WHERE id IN
    (SELECT id
    FROM 
        (SELECT id,
         ROW_NUMBER() OVER( PARTITION BY targetentityid, entityid,
         event
        ORDER BY  id ) AS row_num
        FROM pio_event_1 WHERE event='view') t
        WHERE t.row_num > 1 );
```


