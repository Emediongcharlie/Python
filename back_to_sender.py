def riders_wages(deliveries):
	if deliveries >= 70:
		wages = 500 * deliveries +5000
	if deliveries >= 60 and deliveries <= 69:
		wages = 250 * deliveries + 5000
	if deliveries >= 50 and deliveries <= 59:
		wages = 200 * deliveries + 5000
	if deliveries < 50:
		wages = 160 * deliveries + 5000

	return wages