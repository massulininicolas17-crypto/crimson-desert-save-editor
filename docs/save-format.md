# Crimson Desert `.cdsav` format

Header (little-endian): `4s magic("CDSV") | u16 version | u16 flags | u32 payload_len | u32 crc32`

Payload is a flat section table: repeated `[u16 section_id][u32 length][bytes]`.

Known section IDs seen in community dumps:

| id       | contents                |
|----------|-------------------------|
| `0x0010` | inventory               |
| `0x0020` | skill tree              |
| `0x0030` | world state / flags     |
| `0x0040` | player stats            |

CRC32 is over the payload only (not the header). Writing a save without
recomputing the CRC will make the game reject it.