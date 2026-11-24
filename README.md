# dnssec-simulation

## Overview

### DNS Record Structure

A DNS record contains the following data:
- `owner_name` (ex: `www.example.com`)
- `record_type` (ex: `A`)
- `record_data` (ex: `192.168.1.10`)

The query will contain the following data:
- `type` (ex: `DNS_QUERY`)
- `transation_id` (UUID)
- the record






