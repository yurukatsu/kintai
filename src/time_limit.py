from variable import Time

# Legal working hours
LEGAL_HOURS = {
    28: Time(160, 0),
    29: Time(165, 40),
    30: Time(171, 20),
    31: Time(177, 5)
}

# Outside legal working hours
OUT_LEGAL_OURS = Time(45, 0)