import mpmath

mpmath.mp.prec = 128


def f0(x):
    # airy_Ai
    return mpmath.airyai(x)


def f1(x):
    # airy_Bi
    return mpmath.airybi(x)


def f2(x):
    # airy_Ai_scaled
    scale = mpmath.exp(mpmath.mpf(2) / mpmath.mpf(3) * mpmath.sqrt(x) * x)
    y = mpmath.airyai(x)
    if x > 0.0:
        y = y * scale
    return y


def f3(x):
    # airy_Bi_scaled
    scale = mpmath.exp(-mpmath.mpf(2) / mpmath.mpf(3) * mpmath.sqrt(x) * x)
    y = mpmath.airybi(x)
    if x > 0.0:
        y = y * scale
    return y


def f4(x):
    # airy_Ai_deriv
    return mpmath.airyai(x, derivative=1)


def f5(x):
    # airy_Bi_deriv
    return mpmath.airybi(x, derivative=1)


def f6(x):
    # airy_Ai_deriv_scaled
    scale = mpmath.exp(mpmath.mpf(2) / mpmath.mpf(3) * mpmath.sqrt(x) * x)
    y = mpmath.airyai(x, derivative=1)
    if x > 0.0:
        y = y * scale
    return y


def f7(x):
    # airy_Bi_deriv_scaled
    scale = mpmath.exp(-mpmath.mpf(2) / mpmath.mpf(3) * mpmath.sqrt(x) * x)
    y = mpmath.airybi(x, derivative=1)
    if x > 0.0:
        y = y * scale
    return y


def f8(x):
    # bessel_J0
    return mpmath.besselj(0, x)


def f9(x):
    # bessel_J1
    return mpmath.besselj(1, x)


def f10(x):
    # bessel_Y0
    return mpmath.bessely(0, x)


def f11(x):
    # bessel_Y1
    return mpmath.bessely(1, x)


def f12(x):
    # bessel_I0
    return mpmath.besseli(0, x)


def f13(x):
    # bessel_I1
    return mpmath.besseli(1, x)


def f14(x):
    # bessel_I0_scaled
    scale = mpmath.exp(-abs(x))
    y = mpmath.besseli(0, x) * scale
    return y


def f15(x):
    # bessel_I1_scaled
    scale = mpmath.exp(-abs(x))
    y = mpmath.besseli(1, x) * scale
    return y


def f16(x):
    # bessel_K0
    return mpmath.besselk(0, x)


def f17(x):
    # bessel_K1
    return mpmath.besselk(1, x)


def f18(x):
    # bessel_K0_scaled
    scale = mpmath.exp(x)
    return mpmath.besselk(0, x) * scale


def f19(x):
    # bessel_K1_scaled
    scale = mpmath.exp(x)
    return mpmath.besselk(1, x) * scale


def f20(x):
    # bessel_j0
    x = mpmath.mpf(x)
    return mpmath.sin(x) / x


def f21(x):
    # bessel_j1
    x = mpmath.mpf(x)
    y = (mpmath.sin(x) / x - mpmath.cos(x)) / x
    return y


def f22(x):
    # bessel_j2
    x = mpmath.mpf(x)
    y = ((3 / (x * x) - 1) * mpmath.sin(x) - 3 * mpmath.cos(x) / x) / x
    return y


def f23(x):
    # bessel_y0
    x = mpmath.mpf(x)
    return -mpmath.cos(x) / x


def f24(x):
    # bessel_y1
    x = mpmath.mpf(x)
    return -(mpmath.cos(x) / x + mpmath.sin(x)) / x


def f25(x):
    # bessel_y2
    x = mpmath.mpf(x)
    y = (-3 / (x * x * x) + 1 / x) * mpmath.cos(x) - (3 / (x * x)) * mpmath.sin(x)
    return y


def f26(x):
    # bessel_i0_scaled
    x = mpmath.mpf(x)
    y = mpmath.sqrt(mpmath.pi / (2 * x)) * mpmath.besseli(0.5, x) * mpmath.exp(-abs(x))
    return y


def f27(x):
    # bessel_i1_scaled
    x = mpmath.mpf(x)
    y = mpmath.sqrt(mpmath.pi / (2 * x)) * mpmath.besseli(1.5, x) * mpmath.exp(-abs(x))
    return y


def f28(x):
    # bessel_i2_scaled
    x = mpmath.mpf(x)
    y = mpmath.sqrt(mpmath.pi / (2 * x)) * mpmath.besseli(2.5, x) * mpmath.exp(-abs(x))


def f29(x):
    # bessel_k0_scaled
    x = mpmath.mpf(x)
    y = mpmath.sqrt(mpmath.pi / (2 * x)) * mpmath.besselk(0.5, x) * mpmath.exp(x)
    return y


def f30(x):
    # bessel_k1_scaled
    x = mpmath.mpf(x)
    y = mpmath.sqrt(mpmath.pi / (2 * x)) * mpmath.besselk(1.5, x) * mpmath.exp(x)
    return y


def f31(x):
    # bessel_k2_scaled
    x = mpmath.mpf(x)
    y = mpmath.sqrt(mpmath.pi / (2 * x)) * mpmath.besselk(2.5, x) * mpmath.exp(x)
    return y


def f32(x):
    # clausen
    return mpmath.clsin(2, x)


def f40(x):
    # dilog
    return mpmath.polylog(2, x)


def f41(x):
    # ellint_Kcomp
    x = mpmath.mpf(x)
    return mpmath.ellipk(x * x)


def f42(x):
    # ellint_Ecomp
    x = mpmath.mpf(x)
    return mpmath.ellipe(x * x)


def f44(x):
    # erfc
    return mpmath.erfc(x)


def f45(x):
    # log_erfc
    return mpmath.log(mpmath.erfc(x))


def f46(x):
    # erf
    return mpmath.erf(x)


def f47(x):
    # erf_Z
    return mpmath.npdf(x)


def f48(x):
    # erf_Q
    return 1 - mpmath.ncdf(x)


def f49(x):
    # hazard
    return mpmath.npdf(x) / (1 - mpmath.ncdf(x))


def f50(x):
    # exp
    return mpmath.exp(x)


def f51(x):
    # expm1
    return mpmath.expm1(x)


def f52(x):
    # exprel
    x = mpmath.mpf(x)
    return mpmath.expm1(x) / x


def f53(x):
    # exprel_2
    try:
        x = mpmath.mpf(x)
        y = 2 * (mpmath.expm1(x) - x) / (x * x)
        return y
    except:
        return 0


def f54(x):
    # expint_E1
    return mpmath.expint(1, x)


def f55(x):
    # expint_E2
    return mpmath.expint(2, x)


def f56(x):
    # expint_E1_scaled
    return mpmath.expint(1, x) * mpmath.exp(x)


def f57(x):
    # expint_E2_scaled
    return mpmath.expint(2, x) * mpmath.exp(x)


def f58(x):
    # expint_Ei
    return mpmath.ei(x)


def f59(x):
    # expint_Ei_scaled
    return mpmath.ei(x) * mpmath.exp(-x)


def f60(x):
    # Shi
    return mpmath.shi(x)


def f61(x):
    # Chi
    return mpmath.chi(x)


def f63(x):
    # Si
    return mpmath.si(x)


def f64(x):
    # Ci
    return mpmath.ci(x)


def f66(x):
    # fermi_dirac_m1
    return -mpmath.polylog(0, -mpmath.exp(x))


def f67(x):
    # fermi_dirac_0
    return -mpmath.polylog(1, -mpmath.exp(x))


def f68(x):
    # fermi_dirac_1
    return -mpmath.polylog(2, -mpmath.exp(x))


def f69(x):
    # fermi_dirac_2
    return -mpmath.polylog(3, -mpmath.exp(x))


def f70(x):
    # fermi_dirac_mhalf
    return -mpmath.polylog(0.5, -mpmath.exp(x))


def f71(x):
    # fermi_dirac_half
    try:
        return -mpmath.polylog(1.5, -mpmath.exp(x))
    except:
        return None


def f72(x):
    # fermi_dirac_3half
    try:
        return -mpmath.polylog(2.5, -mpmath.exp(x))
    except:
        return None


def f73(x):
    # lngamma
    try:
        return mpmath.loggamma(x)
    except:
        return None


def f74(x):
    # gamma
    try:
        return mpmath.gamma(x)
    except:
        return None


def f76(x):
    # gammainv
    try:
        return mpmath.rgamma(x)
    except:
        return None


def f77(x):
    # lambert_W0
    return mpmath.lambertw(x)


def f78(x):
    # lambert_Wm1
    if x >= 0:
        return mpmath.lambertw(x)
    else:
        return mpmath.lambertw(x, -1)


def f79(x):
    # legendre_P1
    return mpmath.legendre(1, x)


def f80(x):
    # legendre_P2
    return mpmath.legendre(2, x)


def f81(x):
    # legendre_P3
    return mpmath.legendre(3, x)


def f82(x):
    # legendre_Q0
    return mpmath.legenq(0, 0, x)


def f83(x):
    # legendre_Q1
    return mpmath.legenq(1, 0, x)


def f84(x):
    # log
    return mpmath.log(x)


def f85(x):
    # log_abs
    return mpmath.log(abs(x))


def f86(x):
    # log_1plusx
    return mpmath.log1p(x)


def f87(x):
    # log_1plusx_mx
    x = mpmath.mpf(x)
    return mpmath.log1p(x) - x


def f88(x):
    # psi
    if abs(x) > 1e100:
        return None
    try:
        return mpmath.psi(0, x)
    except:
        return None


def f90(x):
    # psi_1
    if abs(x) > 1e100:
        return None
    try:
        return mpmath.psi(1, x)
    except:
        return None


def f94(x):
    # synchrotron_2
    x = mpmath.mpf(x)
    coff = mpmath.mpf(2) / mpmath.mpf(3)
    return x * mpmath.besselk(coff, x)


def f99(x):
    # sin
    return mpmath.sin(x)


def f100(x):
    # cos
    return mpmath.cos(x)


def f101(x):
    # sinc
    return mpmath.sincpi(x)


def f102(x):
    # lnsinh
    return mpmath.log(mpmath.sinh(x))


def f103(x):
    # lncosh
    return mpmath.log(mpmath.cosh(x))


def f104(x):
    # zeta
    return mpmath.zeta(x)


def f105(x):
    # zetam1
    return mpmath.zeta(x) - 1


def f106(x):
    # eta
    return mpmath.altzeta(x)


func_dict = {
    0: {"direct_support": True, "support": True, "func": f0},
    1: {"direct_support": True, "support": True, "func": f1},
    2: {"direct_support": False, "support": True, "func": f2},
    3: {"direct_support": False, "support": True, "func": f3},
    4: {"direct_support": True, "support": True, "func": f4},
    5: {"direct_support": True, "support": True, "func": f5},
    6: {"direct_support": False, "support": True, "func": f6},
    7: {"direct_support": False, "support": True, "func": f7},
    8: {"direct_support": True, "support": True, "func": f8},
    9: {"direct_support": True, "support": True, "func": f9},
    10: {"direct_support": True, "support": True, "func": f10},
    11: {"direct_support": True, "support": True, "func": f11},
    12: {"direct_support": True, "support": True, "func": f12},
    13: {"direct_support": True, "support": True, "func": f13},
    14: {"direct_support": False, "support": True, "func": f14},
    15: {"direct_support": False, "support": True, "func": f15},
    16: {"direct_support": True, "support": True, "func": f16},
    17: {"direct_support": True, "support": True, "func": f17},
    18: {"direct_support": False, "support": True, "func": f18},
    19: {"direct_support": False, "support": True, "func": f19},
    20: {"direct_support": False, "support": True, "func": f20},
    21: {"direct_support": False, "support": True, "func": f21},
    22: {"direct_support": False, "support": True, "func": f22},
    23: {"direct_support": False, "support": True, "func": f23},
    24: {"direct_support": False, "support": True, "func": f24},
    25: {"direct_support": False, "support": True, "func": f25},
    26: {"direct_support": False, "support": True, "func": f26},
    27: {"direct_support": False, "support": True, "func": f27},
    28: {"direct_support": False, "support": True, "func": f28},
    29: {"direct_support": False, "support": True, "func": f29},
    30: {"direct_support": False, "support": True, "func": f30},
    31: {"direct_support": False, "support": True, "func": f31},
    32: {"direct_support": True, "support": True, "func": f32},
    33: {"direct_support": False, "support": False},
    34: {"direct_support": False, "support": False},
    35: {"direct_support": False, "support": False},
    36: {"direct_support": False, "support": False},
    37: {"direct_support": False, "support": False},
    38: {"direct_support": False, "support": False},
    39: {"direct_support": False, "support": False},
    40: {"direct_support": True, "support": True, "func": f40},
    41: {"direct_support": True, "support": True, "func": f41},
    42: {"direct_support": True, "support": True, "func": f42},
    43: {"direct_support": False, "support": False},
    44: {"direct_support": True, "support": True, "func": f44},
    45: {"direct_support": False, "support": True, "func": f45},
    46: {"direct_support": True, "support": True, "func": f46},
    47: {"direct_support": True, "support": True, "func": f47},
    48: {"direct_support": True, "support": True, "func": f48},
    49: {"direct_support": False, "support": True, "func": f49},
    50: {"direct_support": True, "support": True, "func": f50},
    51: {"direct_support": True, "support": True, "func": f51},
    52: {"direct_support": False, "support": True, "func": f52},
    53: {"direct_support": False, "support": True, "func": f53},
    54: {"direct_support": True, "support": True, "func": f54},
    55: {"direct_support": True, "support": True, "func": f55},
    56: {"direct_support": False, "support": True, "func": f56},
    57: {"direct_support": False, "support": True, "func": f57},
    58: {"direct_support": True, "support": True, "func": f58},
    59: {"direct_support": False, "support": True, "func": f59},
    60: {"direct_support": True, "support": True, "func": f60},
    61: {"direct_support": True, "support": True, "func": f61},
    62: {"direct_support": False, "support": False},
    63: {"direct_support": True, "support": True, "func": f63},
    64: {"direct_support": True, "support": True, "func": f64},
    65: {"direct_support": False, "support": False},
    66: {"direct_support": False, "support": True, "func": f66},
    67: {"direct_support": False, "support": True, "func": f67},
    68: {"direct_support": False, "support": True, "func": f68},
    69: {"direct_support": False, "support": True, "func": f69},
    70: {"direct_support": False, "support": True, "func": f70},
    71: {"direct_support": False, "support": True, "func": f71},
    72: {"direct_support": False, "support": True, "func": f72},
    73: {"direct_support": True, "support": True, "func": f73},
    74: {"direct_support": True, "support": True, "func": f74},
    75: {"direct_support": False, "support": False},
    76: {"direct_support": True, "support": True, "func": f76},
    77: {"direct_support": True, "support": True, "func": f77},
    78: {"direct_support": True, "support": True, "func": f78},
    79: {"direct_support": True, "support": True, "func": f79},
    80: {"direct_support": True, "support": True, "func": f80},
    81: {"direct_support": True, "support": True, "func": f81},
    82: {"direct_support": True, "support": True, "func": f82},
    83: {"direct_support": True, "support": True, "func": f83},
    84: {"direct_support": True, "support": True, "func": f84},
    85: {"direct_support": False, "support": True, "func": f85},
    86: {"direct_support": True, "support": True, "func": f86},
    87: {"direct_support": False, "support": True, "func": f87},
    88: {"direct_support": True, "support": True, "func": f88},
    89: {"direct_support": False, "support": False},
    90: {"direct_support": True, "support": True, "func": f90},
    91: {"direct_support": False, "support": False},
    92: {"direct_support": False, "support": False},
    93: {"direct_support": False, "support": False},
    94: {"direct_support": False, "support": True, "func": f94},
    95: {"direct_support": False, "support": False},
    96: {"direct_support": False, "support": False},
    97: {"direct_support": False, "support": False},
    98: {"direct_support": False, "support": False},
    99: {"direct_support": True, "support": True, "func": f99},
    100: {"direct_support": True, "support": True, "func": f100},
    101: {"direct_support": True, "support": True, "func": f101},
    102: {"direct_support": False, "support": True, "func": f102},
    103: {"direct_support": False, "support": True, "func": f103},
    104: {"direct_support": True, "support": True, "func": f104},
    105: {"direct_support": False, "support": True, "func": f105},
    106: {"direct_support": True, "support": True, "func": f106},
}


func_names = [
    "gsl_sf_airy_Ai_e",
    "gsl_sf_airy_Bi_e",
    "gsl_sf_airy_Ai_scaled_e",
    "gsl_sf_airy_Bi_scaled_e",
    "gsl_sf_airy_Ai_deriv_e",
    "gsl_sf_airy_Bi_deriv_e",
    "gsl_sf_airy_Ai_deriv_scaled_e",
    "gsl_sf_airy_Bi_deriv_scaled_e",
    "gsl_sf_bessel_J0_e",
    "gsl_sf_bessel_J1_e",
    "gsl_sf_bessel_Y0_e",
    "gsl_sf_bessel_Y1_e",
    "gsl_sf_bessel_I0_e",
    "gsl_sf_bessel_I1_e",
    "gsl_sf_bessel_I0_scaled_e",
    "gsl_sf_bessel_I1_scaled_e",
    "gsl_sf_bessel_K0_e",
    "gsl_sf_bessel_K1_e",
    "gsl_sf_bessel_K0_scaled_e",
    "gsl_sf_bessel_K1_scaled_e",
    "gsl_sf_bessel_j0_e",
    "gsl_sf_bessel_j1_e",
    "gsl_sf_bessel_j2_e",
    "gsl_sf_bessel_y0_e",
    "gsl_sf_bessel_y1_e",
    "gsl_sf_bessel_y2_e",
    "gsl_sf_bessel_i0_scaled_e",
    "gsl_sf_bessel_i1_scaled_e",
    "gsl_sf_bessel_i2_scaled_e",
    "gsl_sf_bessel_k0_scaled_e",
    "gsl_sf_bessel_k1_scaled_e",
    "gsl_sf_bessel_k2_scaled_e",
    "gsl_sf_clausen_e",
    "gsl_sf_dawson_e",
    "gsl_sf_debye_1_e",
    "gsl_sf_debye_2_e",
    "gsl_sf_debye_3_e",
    "gsl_sf_debye_4_e",
    "gsl_sf_debye_5_e",
    "gsl_sf_debye_6_e",
    "gsl_sf_dilog_e",
    "gsl_sf_ellint_Kcomp_e",
    "gsl_sf_ellint_Ecomp_e",
    "gsl_sf_ellint_Dcomp_e",
    "gsl_sf_erfc_e",
    "gsl_sf_log_erfc_e",
    "gsl_sf_erf_e",
    "gsl_sf_erf_Z_e",
    "gsl_sf_erf_Q_e",
    "gsl_sf_hazard_e",
    "gsl_sf_exp_e",
    "gsl_sf_expm1_e",
    "gsl_sf_exprel_e",
    "gsl_sf_exprel_2_e",
    "gsl_sf_expint_E1_e",
    "gsl_sf_expint_E2_e",
    "gsl_sf_expint_E1_scaled_e",
    "gsl_sf_expint_E2_scaled_e",
    "gsl_sf_expint_Ei_e",
    "gsl_sf_expint_Ei_scaled_e",
    "gsl_sf_Shi_e",
    "gsl_sf_Chi_e",
    "gsl_sf_expint_3_e",
    "gsl_sf_Si_e",
    "gsl_sf_Ci_e",
    "gsl_sf_atanint_e",
    "gsl_sf_fermi_dirac_m1_e",
    "gsl_sf_fermi_dirac_0_e",
    "gsl_sf_fermi_dirac_1_e",
    "gsl_sf_fermi_dirac_2_e",
    "gsl_sf_fermi_dirac_mhalf_e",
    "gsl_sf_fermi_dirac_half_e",
    "gsl_sf_fermi_dirac_3half_e",
    "gsl_sf_lngamma_e",
    "gsl_sf_gamma_e",
    "gsl_sf_gammastar_e",
    "gsl_sf_gammainv_e",
    "gsl_sf_lambert_W0_e",
    "gsl_sf_lambert_Wm1_e",
    "gsl_sf_legendre_P1_e",
    "gsl_sf_legendre_P2_e",
    "gsl_sf_legendre_P3_e",
    "gsl_sf_legendre_Q0_e",
    "gsl_sf_legendre_Q1_e",
    "gsl_sf_log_e",
    "gsl_sf_log_abs_e",
    "gsl_sf_log_1plusx_e",
    "gsl_sf_log_1plusx_mx_e",
    "gsl_sf_psi_e",
    "gsl_sf_psi_1piy_e",
    "gsl_sf_psi_1_e",
    "gsl_sf_sin_pi_e",
    "gsl_sf_cos_pi_e",
    "gsl_sf_synchrotron_1_e",
    "gsl_sf_synchrotron_2_e",
    "gsl_sf_transport_2_e",
    "gsl_sf_transport_3_e",
    "gsl_sf_transport_4_e",
    "gsl_sf_transport_5_e",
    "gsl_sf_sin_e",
    "gsl_sf_cos_e",
    "gsl_sf_sinc_e",
    "gsl_sf_lnsinh_e",
    "gsl_sf_lncosh_e",
    "gsl_sf_zeta_e",
    "gsl_sf_zetam1_e",
    "gsl_sf_eta_e",
]
