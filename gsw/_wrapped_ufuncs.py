
"""
Auto-generated wrapper for C ufunc extension; do not edit!
"""

#from ._wrapped_ufuncs import *
from . import _gsw_ufuncs
from ._utilities import match_args_return


@match_args_return
def adiabatic_lapse_rate_from_CT(SA, CT, p):
    """
    Calculates the adiabatic lapse rate of sea water from Conservative
    Temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    adiabatic_lapse_rate : array-like, K/Pa
        Note.  The output is in unit of degress Celsius per Pa,
        (or equivilently K/Pa) not in units of K/dbar.
        

    """
    return _gsw_ufuncs.adiabatic_lapse_rate_from_ct(SA, CT, p)

@match_args_return
def adiabatic_lapse_rate_ice(t, p):
    """
    Calculates the adiabatic lapse rate of ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    adiabatic_lapse_rate_ice : array-like, K/Pa
        Note.  The output is in unit of degress Celsius per Pa,
        (or equivilently K/Pa) not in units of K/dbar.
        

    """
    return _gsw_ufuncs.adiabatic_lapse_rate_ice(t, p)

@match_args_return
def alpha(SA, CT, p):
    """
    Calculates the thermal expansion coefficient of seawater with respect to
    Conservative Temperature using the computationally-efficient expression
    for specific volume in terms of SA, CT and p (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    alpha : array-like, 1/K
        with respect to Conservative Temperature
        

    """
    return _gsw_ufuncs.alpha(SA, CT, p)

@match_args_return
def alpha_on_beta(SA, CT, p):
    """
    Calculates alpha divided by beta, where alpha is the thermal expansion
    coefficient and beta is the saline contraction coefficient of seawater
    from Absolute Salinity and Conservative Temperature.  This function uses
    the computationally-efficient expression for specific volume in terms of
    SA, CT and p (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    alpha_on_beta : array-like, kg g^-1 K^-1
        Conservative Temperature divided by the saline
        contraction coefficient at constant Conservative
        Temperature
        

    """
    return _gsw_ufuncs.alpha_on_beta(SA, CT, p)

@match_args_return
def alpha_wrt_t_exact(SA, t, p):
    """
    Calculates the thermal expansion coefficient of seawater with respect to
    in-situ temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    alpha_wrt_t_exact : array-like, 1/K
        with respect to in-situ temperature
        

    """
    return _gsw_ufuncs.alpha_wrt_t_exact(SA, t, p)

@match_args_return
def alpha_wrt_t_ice(t, p):
    """
    Calculates the thermal expansion coefficient of ice with respect to
    in-situ temperature.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    alpha_wrt_t_ice : array-like, 1/K
        to in-situ temperature
        

    """
    return _gsw_ufuncs.alpha_wrt_t_ice(t, p)

@match_args_return
def beta(SA, CT, p):
    """
    Calculates the saline (i.e. haline) contraction coefficient of seawater
    at constant Conservative Temperature using the computationally-efficient
    75-term expression for specific volume in terms of SA, CT and p
    (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    beta : array-like, kg/g
        at constant Conservative Temperature
        

    """
    return _gsw_ufuncs.beta(SA, CT, p)

@match_args_return
def beta_const_t_exact(SA, t, p):
    """
    Calculates the saline (i.e. haline) contraction coefficient of seawater
    at constant in-situ temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    beta_const_t_exact : array-like, kg/g
        at constant in-situ temperature
        

    """
    return _gsw_ufuncs.beta_const_t_exact(SA, t, p)

@match_args_return
def C_from_SP(SP, t, p):
    """
    Calculates conductivity, C, from (SP,t,p) using PSS-78 in the range
    2 < SP < 42.  If the input Practical Salinity is less than 2 then a
    modified form of the Hill et al. (1986) fomula is used for Practical
    Salinity.  The modification of the Hill et al. (1986) expression is to
    ensure that it is exactly consistent with PSS-78 at SP = 2.

    Parameters
    ----------
    SP : array-like
        Practical Salinity (PSS-78), unitless
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    C : array-like, mS/cm
        

    """
    return _gsw_ufuncs.c_from_sp(SP, t, p)

@match_args_return
def cabbeling(SA, CT, p):
    """
    Calculates the cabbeling coefficient of seawater with respect to
    Conservative Temperature.  This function uses the computationally-
    efficient expression for specific volume in terms of SA, CT and p
    (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    cabbeling : array-like, 1/K^2
        Conservative Temperature.
        

    """
    return _gsw_ufuncs.cabbeling(SA, CT, p)

@match_args_return
def chem_potential_water_ice(t, p):
    """
    Calculates the chemical potential of water in ice from in-situ
    temperature and pressure.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    chem_potential_water_ice : array-like, J/kg
        

    """
    return _gsw_ufuncs.chem_potential_water_ice(t, p)

@match_args_return
def chem_potential_water_t_exact(SA, t, p):
    """
    Calculates the chemical potential of water in seawater.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    chem_potential_water_t_exact : array-like, J/g
        
        

    """
    return _gsw_ufuncs.chem_potential_water_t_exact(SA, t, p)

@match_args_return
def cp_ice(t, p):
    """
    Calculates the isobaric heat capacity of seawater.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    cp_ice : array-like, J kg^-1 K^-1
        

    """
    return _gsw_ufuncs.cp_ice(t, p)

@match_args_return
def cp_t_exact(SA, t, p):
    """
    Calculates the isobaric heat capacity of seawater.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    cp_t_exact : array-like, J/(kg*K)
        

    """
    return _gsw_ufuncs.cp_t_exact(SA, t, p)

@match_args_return
def CT_freezing(SA, p, saturation_fraction):
    """
    Calculates the Conservative Temperature at which seawater freezes.  The
    Conservative Temperature freezing point is calculated from the exact
    in-situ freezing temperature which is found by a modified Newton-Raphson
    iteration (McDougall and Wotherspoon, 2014) of the equality of the
    chemical potentials of water in seawater and in ice.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    CT_freezing : array-like, deg C
        That is, the freezing temperature expressed in terms of
        Conservative Temperature (ITS-90).
        

    """
    return _gsw_ufuncs.ct_freezing(SA, p, saturation_fraction)

@match_args_return
def CT_freezing_poly(SA, p, saturation_fraction):
    """
    Calculates the Conservative Temperature at which seawater freezes.
    The error of this fit ranges between -5e-4 K and 6e-4 K when compared
    with the Conservative Temperature calculated from the exact in-situ
    freezing temperature which is found by a Newton-Raphson iteration of the
    equality of the chemical potentials of water in seawater and in ice.
    Note that the Conservative Temperature freezing temperature can be found
    by this exact method using the function gsw_CT_freezing.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    CT_freezing : array-like, deg C
        That is, the freezing temperature expressed in
        terms of Conservative Temperature (ITS-90).
        

    """
    return _gsw_ufuncs.ct_freezing_poly(SA, p, saturation_fraction)

@match_args_return
def CT_from_enthalpy(SA, h, p):
    """
    Calculates the Conservative Temperature of seawater, given the Absolute
    Salinity, specific enthalpy, h, and pressure p.  The specific enthalpy
    input is the one calculated from the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    h : array-like
        Specific enthalpy, J/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    CT : array-like, deg C
        

    """
    return _gsw_ufuncs.ct_from_enthalpy(SA, h, p)

@match_args_return
def CT_from_enthalpy_exact(SA, h, p):
    """
    Calculates the Conservative Temperature of seawater, given the Absolute
    Salinity, SA, specific enthalpy, h, and pressure p.  The specific
    enthalpy input is calculated from the full Gibbs function of seawater,
    gsw_enthalpy_t_exact.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    h : array-like
        Specific enthalpy, J/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    CT : array-like, deg C
        

    """
    return _gsw_ufuncs.ct_from_enthalpy_exact(SA, h, p)

@match_args_return
def CT_from_entropy(SA, entropy):
    """
    Calculates Conservative Temperature with entropy as an input variable.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    entropy : array-like
        Specific entropy, J/(kg*K)

    Returns
    -------
    CT : array-like, deg C
        

    """
    return _gsw_ufuncs.ct_from_entropy(SA, entropy)

@match_args_return
def CT_from_pt(SA, pt):
    """
    Calculates Conservative Temperature of seawater from potential
    temperature (whose reference sea pressure is zero dbar).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    pt : array-like
        Potential temperature referenced to a sea pressure, degrees C

    Returns
    -------
    CT : array-like, deg C
        

    """
    return _gsw_ufuncs.ct_from_pt(SA, pt)

@match_args_return
def CT_from_t(SA, t, p):
    """
    Calculates Conservative Temperature of seawater from in-situ
    temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    CT : array-like, deg C
        

    """
    return _gsw_ufuncs.ct_from_t(SA, t, p)

@match_args_return
def CT_maxdensity(SA, p):
    """
    Calculates the Conservative Temperature of maximum density of seawater.
    This function returns the Conservative temperature at which the density
    of seawater is a maximum, at given Absolute Salinity, SA, and sea
    pressure, p (in dbar).  This function uses the computationally-efficient
    expression for specific volume in terms of SA, CT and p
    (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    CT_maxdensity : array-like, deg C
        the density of seawater is a maximum for
        given Absolute Salinity and pressure.
        

    """
    return _gsw_ufuncs.ct_maxdensity(SA, p)

@match_args_return
def deltaSA_atlas(p, lon, lat):
    """
    Calculates the Absolute Salinity Anomaly atlas value, SA - SR, in
    the open ocean by spatially interpolating the global reference data set
    of deltaSA_atlas to the location of the seawater sample.

    Parameters
    ----------
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    deltaSA_atlas : array-like, g/kg
        in_ocean        =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.deltasa_atlas(p, lon, lat)

@match_args_return
def deltaSA_from_SP(SP, p, lon, lat):
    """
    Calculates Absolute Salinity Anomaly from Practical Salinity.  Since SP
    is non-negative by definition, this function changes any negative input
    values of SP to be zero.

    Parameters
    ----------
    SP : array-like
        Practical Salinity (PSS-78), unitless
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    deltaSA : array-like, g/kg
        

    """
    return _gsw_ufuncs.deltasa_from_sp(SP, p, lon, lat)

@match_args_return
def dilution_coefficient_t_exact(SA, t, p):
    """
    Calculates the dilution coefficient of seawater.  The dilution
    coefficient of seawater is defined as the Absolute Salinity times the
    second derivative of the Gibbs function with respect to Absolute
    Salinity, that is, SA.*g_SA_SA.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    dilution_coefficient_t_exact : array-like, (J/kg)(kg/g)
        

    """
    return _gsw_ufuncs.dilution_coefficient_t_exact(SA, t, p)

@match_args_return
def dynamic_enthalpy(SA, CT, p):
    """
    Calculates dynamic enthalpy of seawater using the computationally-
    efficient expression for specific volume in terms of SA, CT and p
    (Roquet et al., 2015).  Dynamic enthalpy is defined as enthalpy minus
    potential enthalpy (Young, 2010).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    dynamic_enthalpy : array-like, J/kg
        

    """
    return _gsw_ufuncs.dynamic_enthalpy(SA, CT, p)

@match_args_return
def enthalpy(SA, CT, p):
    """
    Calculates specific enthalpy of seawater using the computationally-
    efficient expression for specific volume in terms of SA, CT and p
    (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    enthalpy : array-like, J/kg
        

    """
    return _gsw_ufuncs.enthalpy(SA, CT, p)

@match_args_return
def enthalpy_CT_exact(SA, CT, p):
    """
    Calculates specific enthalpy of seawater from Absolute Salinity and
    Conservative Temperature and pressure.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    enthalpy_CT_exact : array-like, J/kg
        

    """
    return _gsw_ufuncs.enthalpy_ct_exact(SA, CT, p)

@match_args_return
def enthalpy_diff(SA, CT, p_shallow, p_deep):
    """
    Calculates the difference of the specific enthalpy of seawater between
    two different pressures, p_deep (the deeper pressure) and p_shallow
    (the shallower pressure), at the same values of SA and CT.  This
    function uses the computationally-efficient expression for specific
    volume in terms of SA, CT and p (Roquet et al., 2015).  The output
    (enthalpy_diff) is the specific enthalpy evaluated at (SA,CT,p_deep)
    minus the specific enthalpy at (SA,CT,p_shallow).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p_shallow : array-like
        Upper sea pressure (absolute pressure minus 10.1325 dbar), dbar
    p_deep : array-like
        Lower sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    enthalpy_diff : array-like, J/kg
        (deep minus shallow)
        

    """
    return _gsw_ufuncs.enthalpy_diff(SA, CT, p_shallow, p_deep)

@match_args_return
def enthalpy_ice(t, p):
    """
    Calculates the specific enthalpy of ice (h_Ih).

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    enthalpy_ice : array-like, J/kg
        

    """
    return _gsw_ufuncs.enthalpy_ice(t, p)

@match_args_return
def enthalpy_SSO_0(p):
    """
    (no description available)
    """
    return _gsw_ufuncs.enthalpy_sso_0(p)

@match_args_return
def enthalpy_t_exact(SA, t, p):
    """
    Calculates the specific enthalpy of seawater.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    enthalpy_t_exact : array-like, J/kg
        

    """
    return _gsw_ufuncs.enthalpy_t_exact(SA, t, p)

@match_args_return
def entropy_from_pt(SA, pt):
    """
    Calculates specific entropy of seawater as a function of potential
    temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    pt : array-like
        Potential temperature referenced to a sea pressure, degrees C

    Returns
    -------
    entropy : array-like, J/(kg*K)
        

    """
    return _gsw_ufuncs.entropy_from_pt(SA, pt)

@match_args_return
def entropy_from_t(SA, t, p):
    """
    Calculates specific entropy of seawater from in-situ temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    entropy : array-like, J/(kg*K)
        

    """
    return _gsw_ufuncs.entropy_from_t(SA, t, p)

@match_args_return
def entropy_ice(t, p):
    """
    Calculates specific entropy of ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    ice_entropy : array-like, J kg^-1 K^-1
        

    """
    return _gsw_ufuncs.entropy_ice(t, p)

@match_args_return
def entropy_part(SA, t, p):
    """
    (no description available)
    """
    return _gsw_ufuncs.entropy_part(SA, t, p)

@match_args_return
def entropy_part_zerop(SA, pt0):
    """
    (no description available)
    """
    return _gsw_ufuncs.entropy_part_zerop(SA, pt0)

@match_args_return
def Fdelta(p, lon, lat):
    """
    Calculates Fdelta from the Absolute Salinity Anomaly Ratio (SAAR).  It
    finds SAAR by calling the function "gsw_SAAR(p,long,lat)" and then
    simply calculates Fdelta from

    Parameters
    ----------
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    Fdelta : array-like, unitless
        

    """
    return _gsw_ufuncs.fdelta(p, lon, lat)

@match_args_return
def gibbs_ice_part_t(t, p):
    """
    part of the the first temperature derivative of Gibbs energy of ice
    that is the outout is gibbs_ice(1,0,t,p) + S0

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    gibbs_ice_part_t : array-like, J kg^-1 K^-1
        

    """
    return _gsw_ufuncs.gibbs_ice_part_t(t, p)

@match_args_return
def gibbs_ice_pt0(pt0):
    """
    part of the the first temperature derivative of Gibbs energy of ice
    that is the outout is "gibbs_ice(1,0,pt0,0) + s0"

    Parameters
    ----------
    pt0 : array-like
        Potential temperature with reference pressure of 0 dbar, degrees C

    Returns
    -------
    gibbs_ice_part_pt0 : array-like, J kg^-1 K^-1
        

    """
    return _gsw_ufuncs.gibbs_ice_pt0(pt0)

@match_args_return
def gibbs_ice_pt0_pt0(pt0):
    """
    The second temperature derivative of Gibbs energy of ice at the
    potential temperature with reference sea pressure of zero dbar.  That is
    the output is gibbs_ice(2,0,pt0,0).

    Parameters
    ----------
    pt0 : array-like
        Potential temperature with reference pressure of 0 dbar, degrees C

    Returns
    -------
    gibbs_ice_pt0_pt0 : array-like, J kg^-1 K^-2
        
        

    """
    return _gsw_ufuncs.gibbs_ice_pt0_pt0(pt0)

@match_args_return
def gibbs_pt0_pt0(SA, pt0):
    """
    (no description available)
    """
    return _gsw_ufuncs.gibbs_pt0_pt0(SA, pt0)

@match_args_return
def grav(lat, p):
    """
    Calculates acceleration due to gravity as a function of latitude and as
    a function of pressure in the ocean.

    Parameters
    ----------
    lat : array-like
        Latitude, -90 to 90 degrees
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    grav : array-like, m s^-2
        

    """
    return _gsw_ufuncs.grav(lat, p)

@match_args_return
def Helmholtz_energy_ice(t, p):
    """
    Calculates the Helmholtz energy of ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    Helmholtz_energy_ice : array-like, J/kg
        

    """
    return _gsw_ufuncs.helmholtz_energy_ice(t, p)

@match_args_return
def Hill_ratio_at_SP2(t):
    """
    Calculates the Hill ratio, which is the adjustment needed to apply for
    Practical Salinities smaller than 2.  This ratio is defined at a
    Practical Salinity = 2 and in-situ temperature, t using PSS-78. The Hill
    ratio is the ratio of 2 to the output of the Hill et al. (1986) formula
    for Practical Salinity at the conductivity ratio, Rt, at which Practical
    Salinity on the PSS-78 scale is exactly 2.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C

    Returns
    -------
    Hill_ratio : array-like, unitless
        

    """
    return _gsw_ufuncs.hill_ratio_at_sp2(t)

@match_args_return
def internal_energy(SA, CT, p):
    """
    Calculates specific internal energy of seawater using the
    computationally-efficient expression for specific volume in terms of SA,
    CT and p (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    internal_energy : array-like, J/kg
        

    """
    return _gsw_ufuncs.internal_energy(SA, CT, p)

@match_args_return
def internal_energy_ice(t, p):
    """
    Calculates the specific internal energy of ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    internal_energy_ice : array-like, J/kg
        

    """
    return _gsw_ufuncs.internal_energy_ice(t, p)

@match_args_return
def kappa(SA, CT, p):
    """
    Calculates the isentropic compressibility of seawater.  This function
    has inputs of Absolute Salinity and Conservative Temperature.  This
    function uses the computationally-efficient expression for
    specific volume in terms of SA, CT and p (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    kappa : array-like, 1/Pa
        

    """
    return _gsw_ufuncs.kappa(SA, CT, p)

@match_args_return
def kappa_const_t_ice(t, p):
    """
    Calculates isothermal compressibility of ice.
    Note. This is the compressibility of ice AT CONSTANT IN-SITU
    TEMPERATURE

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    kappa_const_t_ice : array-like, 1/Pa
        Note. The output units are 1/Pa not 1/dbar.
        

    """
    return _gsw_ufuncs.kappa_const_t_ice(t, p)

@match_args_return
def kappa_ice(t, p):
    """
    Calculates the isentropic compressibility of ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    kappa_ice : array-like, 1/Pa
        Note. The output units are 1/Pa not 1/dbar.
        

    """
    return _gsw_ufuncs.kappa_ice(t, p)

@match_args_return
def kappa_t_exact(SA, t, p):
    """
    Calculates the isentropic compressibility of seawater.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    kappa_t_exact : array-like, 1/Pa
        Note. The output units are 1/Pa not 1/dbar.
        

    """
    return _gsw_ufuncs.kappa_t_exact(SA, t, p)

@match_args_return
def latentheat_evap_CT(SA, CT):
    """
    Calculates latent heat, or enthalpy, of evaporation at p = 0 (the
    surface).  It is defined as a function of Absolute Salinity, SA, and
    Conservative Temperature, CT, and is valid in the ranges
    0 < SA < 42 g/kg and 0 < CT < 40 deg C.  The errors range between
    -0.4 and 0.6 J/kg.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    latentheat_evap : array-like, J/kg
        

    """
    return _gsw_ufuncs.latentheat_evap_ct(SA, CT)

@match_args_return
def latentheat_evap_t(SA, t):
    """
    Calculates latent heat, or enthalpy, of evaporation at p = 0 (the
    surface).  It is defined as a function of Absolute Salinity, SA, and
    in-situ temperature, t, and is valid in the ranges 0 < SA < 40 g/kg
    and 0 < CT < 42 deg C. The errors range between -0.4 and 0.6 J/kg.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C

    Returns
    -------
    latentheat_evap : array-like, J/kg
        

    """
    return _gsw_ufuncs.latentheat_evap_t(SA, t)

@match_args_return
def latentheat_melting(SA, p):
    """
    Calculates latent heat, or enthalpy, of melting.  It is defined in terms
    of Absolute Salinity, SA, and sea pressure, p, and is valid in the
    ranges 0 < SA < 42 g kg^-1 and 0 < p < 10,000 dbar.  This is based on
    the IAPWS Releases IAPWS-09 (for pure water), IAPWS-08 (for the saline
    compoonent of seawater and IAPWS-06 for ice Ih.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    latentheat_melting : array-like, J/kg
        

    """
    return _gsw_ufuncs.latentheat_melting(SA, p)

@match_args_return
def melting_ice_equilibrium_SA_CT_ratio(SA, p):
    """
    Calculates the ratio of SA to CT changes when ice melts into seawater
    with both the seawater and the seaice temperatures being almost equal to
    the equilibrium freezing temperature.  It is assumed that a small mass
    of ice melts into an infinite mass of seawater.  If indeed the
    temperature of the seawater and the ice were both equal to the freezing
    temperature, then no melting or freezing would occur; an imbalance
    between these three temperatures is needed for freezing or melting to
    occur (the three temperatures being (1) the seawater temperature,
    (2) the ice temperature, and (3) the freezing temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    melting_ice_equilibrium_SA_CT_ratio : array-like, g/(kg K)
        changes when ice melts into seawater, with
        the seawater and seaice being close to the
        freezing temperature.
        

    """
    return _gsw_ufuncs.melting_ice_equilibrium_sa_ct_ratio(SA, p)

@match_args_return
def melting_ice_equilibrium_SA_CT_ratio_poly(SA, p):
    """
    Calculates the ratio of SA to CT changes when ice melts into seawater
    with both the seawater and the seaice temperatures being almost equal to
    the equilibrium freezing temperature.  It is assumed that a small mass
    of ice melts into an infinite mass of seawater.  If indeed the
    temperature of the seawater and the ice were both equal to the freezing
    temperature, then no melting or freezing would occur; an imbalance
    between these three temperatures is needed for freezing or melting to
    occur (the three temperatures being (1) the seawater temperature,
    (2) the ice temperature, and (3) the freezing temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    melting_ice_equilibrium_SA_CT_ratio : array-like, g/(kg K)
        changes when ice melts into seawater, with
        the seawater and seaice being close to the
        freezing temperature.
        

    """
    return _gsw_ufuncs.melting_ice_equilibrium_sa_ct_ratio_poly(SA, p)

@match_args_return
def melting_ice_SA_CT_ratio(SA, CT, p, t_Ih):
    """
    Calculates the ratio of SA to CT changes when ice melts into seawater.
    It is assumed that a small mass of ice melts into an infinite mass of
    seawater.  Because of the infinite mass of seawater, the ice will always
    melt.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    t_Ih : array-like
        In-situ temperature of ice (ITS-90), degrees C

    Returns
    -------
    melting_ice_SA_CT_ratio : array-like, g kg^-1 K^-1
        into a large mass of seawater
        
        

    """
    return _gsw_ufuncs.melting_ice_sa_ct_ratio(SA, CT, p, t_Ih)

@match_args_return
def melting_ice_SA_CT_ratio_poly(SA, CT, p, t_Ih):
    """
    Calculates the ratio of SA to CT changes when ice melts into seawater.
    It is assumed that a small mass of ice melts into an infinite mass of
    seawater.  Because of the infinite mass of seawater, the ice will always
    melt.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    t_Ih : array-like
        In-situ temperature of ice (ITS-90), degrees C

    Returns
    -------
    melting_ice_SA_CT_ratio : array-like, g kg^-1 K^-1
        into a large mass of seawater
        
        

    """
    return _gsw_ufuncs.melting_ice_sa_ct_ratio_poly(SA, CT, p, t_Ih)

@match_args_return
def melting_seaice_equilibrium_SA_CT_ratio(SA, p):
    """
    Calculates the ratio of SA to CT changes when sea ice melts into
    seawater with both the seawater and the sea ice temperatures being
    almost equal to the equilibrium freezing temperature.  It is assumed
    that a small mass of seaice melts into an infinite mass of seawater.  If
    indeed the temperature of the seawater and the sea ice were both equal
    to the freezing temperature, then no melting or freezing would occur; an
    imbalance between these three temperatures is needed for freezing or
    melting to occur (the three temperatures being (1) the seawater
    temperature, (2) the sea ice temperature, and (3) the freezing
    temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    melting_seaice_equilibrium_SA_CT_ratio : array-like, g/(kg K)
        changes when sea ice melts into seawater, with
        the seawater and sea ice being close to the
        freezing temperature.
        

    """
    return _gsw_ufuncs.melting_seaice_equilibrium_sa_ct_ratio(SA, p)

@match_args_return
def melting_seaice_equilibrium_SA_CT_ratio_poly(SA, p):
    """
    Calculates the ratio of SA to CT changes when sea ice melts into
    seawater with both the seawater and the sea ice temperatures being
    almost equal to the equilibrium freezing temperature.  It is assumed
    that a small mass of seaice melts into an infinite mass of seawater.  If
    indeed the temperature of the seawater and the sea ice were both equal
    to the freezing temperature, then no melting or freezing would occur; an
    imbalance between these three temperatures is needed for freezing or
    melting to occur (the three temperatures being (1) the seawater
    temperature, (2) the sea ice temperature, and (3) the freezing
    temperature.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    melting_seaice_equilibrium_SA_CT_ratio : array-like, g/(kg K)
        changes when sea ice melts into seawater, with
        the seawater and sea ice being close to the
        freezing temperature.
        

    """
    return _gsw_ufuncs.melting_seaice_equilibrium_sa_ct_ratio_poly(SA, p)

@match_args_return
def melting_seaice_SA_CT_ratio(SA, CT, p, SA_seaice, t_seaice):
    """
    Calculates the ratio of SA to CT changes when sea ice melts into
    seawater.  It is assumed that a small mass of sea ice melts into an
    infinite mass of seawater.  Because of the infinite mass of seawater,
    the sea ice will always melt.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    SA_seaice : array-like
        Absolute Salinity of sea ice: the mass fraction of salt
        in sea ice, expressed in g of salt per kg of sea ice.
    t_seaice : array-like
        In-situ temperature of the sea ice at pressure p (ITS-90), degrees C

    Returns
    -------
    melting_seaice_SA_CT_ratio : array-like, g/(kg K)
        sea ice melts into a large mass of seawater
        

    """
    return _gsw_ufuncs.melting_seaice_sa_ct_ratio(SA, CT, p, SA_seaice, t_seaice)

@match_args_return
def melting_seaice_SA_CT_ratio_poly(SA, CT, p, SA_seaice, t_seaice):
    """
    Calculates the ratio of SA to CT changes when sea ice melts into
    seawater.  It is assumed that a small mass of sea ice melts into an
    infinite mass of seawater.  Because of the infinite mass of seawater,
    the sea ice will always melt.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    SA_seaice : array-like
        Absolute Salinity of sea ice: the mass fraction of salt
        in sea ice, expressed in g of salt per kg of sea ice.
    t_seaice : array-like
        In-situ temperature of the sea ice at pressure p (ITS-90), degrees C

    Returns
    -------
    melting_seaice_SA_CT_ratio : array-like, g/(kg K)
        sea ice melts into a large mass of seawater
        

    """
    return _gsw_ufuncs.melting_seaice_sa_ct_ratio_poly(SA, CT, p, SA_seaice, t_seaice)

@match_args_return
def pot_enthalpy_from_pt_ice(pt0_ice):
    """
    Calculates the potential enthalpy of ice from potential temperature of
    ice (whose reference sea pressure is zero dbar).

    Parameters
    ----------
    pt0_ice : array-like
        Potential temperature of ice (ITS-90), degrees C

    Returns
    -------
    pot_enthalpy_ice : array-like, J/kg
        

    """
    return _gsw_ufuncs.pot_enthalpy_from_pt_ice(pt0_ice)

@match_args_return
def pot_enthalpy_from_pt_ice_poly(pt0_ice):
    """
    Calculates the potential enthalpy of ice from potential temperature of
    ice (whose reference sea pressure is zero dbar).  This is a
    compuationally efficient polynomial fit to the potential enthalpy of
    ice.

    Parameters
    ----------
    pt0_ice : array-like
        Potential temperature of ice (ITS-90), degrees C

    Returns
    -------
    pot_enthalpy_ice : array-like, J/kg
        

    """
    return _gsw_ufuncs.pot_enthalpy_from_pt_ice_poly(pt0_ice)

@match_args_return
def pot_enthalpy_ice_freezing(SA, p):
    """
    Calculates the potential enthalpy of ice at which seawater freezes.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    pot_enthalpy_ice_freezing : array-like, J/kg
        of seawater
        

    """
    return _gsw_ufuncs.pot_enthalpy_ice_freezing(SA, p)

@match_args_return
def pot_enthalpy_ice_freezing_poly(SA, p):
    """
    Calculates the potential enthalpy of ice at which seawater freezes.
    The error of this fit ranges between -2.5 and 1 J/kg with an rms of
    1.07, between SA of 0 and 120 g/kg and p between 0 and 10,000 dbar (the
    error in the fit is between -0.7 and 0.7 with an rms of
    0.3, between SA of 0 and 120 g/kg and p between 0 and 5,000 dbar) when
    compared with the potential enthalpy calculated from the exact in-situ
    freezing temperature which is found by a Newton-Raphson iteration of the
    equality of the chemical potentials of water in seawater and in ice.
    Note that the potential enthalpy at freezing can be found
    by this exact method using the function gsw_pot_enthalpy_ice_freezing.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    pot_enthalpy_ice_freezing : array-like, J/kg
        of seawater
        

    """
    return _gsw_ufuncs.pot_enthalpy_ice_freezing_poly(SA, p)

@match_args_return
def pot_rho_t_exact(SA, t, p, p_ref):
    """
    Calculates potential density of seawater.  Note. This function outputs
    potential density, not potential density anomaly; that is, 1000 kg/m^3
    is not subtracted.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    p_ref : array-like
        Reference pressure, dbar

    Returns
    -------
    pot_rho_t_exact : array-like, kg/m^3
        
        

    """
    return _gsw_ufuncs.pot_rho_t_exact(SA, t, p, p_ref)

@match_args_return
def pressure_coefficient_ice(t, p):
    """
    Calculates pressure coefficient of ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    pressure_coefficient_ice : array-like, Pa/K
        Note. The output units are Pa/K NOT dbar/K.
        

    """
    return _gsw_ufuncs.pressure_coefficient_ice(t, p)

@match_args_return
def pressure_freezing_CT(SA, CT, saturation_fraction):
    """
    Calculates the pressure (in dbar) of seawater at the freezing
    temperature.  That is, the output is the pressure at which seawater,
    with Absolute Salinity SA, Conservative Temperature CT, and with
    saturation_fraction of dissolved air, freezes.  If the input values are
    such that there is no value of pressure in the range between 0 dbar and
    10,000 dbar for which seawater is at the freezing temperature, the
    output, pressure_freezing, is put equal to NaN.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    pressure_freezing : array-like, dbar
        ( i.e. absolute pressure - 10.1325 dbar )
        

    """
    return _gsw_ufuncs.pressure_freezing_ct(SA, CT, saturation_fraction)

@match_args_return
def pt0_from_t(SA, t, p):
    """
    Calculates potential temperature with reference pressure, p_ref = 0 dbar.
    The present routine is computationally faster than the more general
    function "gsw_pt_from_t(SA,t,p,p_ref)" which can be used for any
    reference pressure value.
    This subroutine calls "gsw_entropy_part(SA,t,p)",
    "gsw_entropy_part_zerop(SA,pt0)" and "gsw_gibbs_pt0_pt0(SA,pt0)".

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    pt0 : array-like, deg C
        with reference sea pressure (p_ref) = 0 dbar.
        Note. The reference sea pressure of the output, pt0, is zero dbar.
        

    """
    return _gsw_ufuncs.pt0_from_t(SA, t, p)

@match_args_return
def pt0_from_t_ice(t, p):
    """
    Calculates potential temperature of ice Ih with a reference pressure of
    0 dbar, from in-situ temperature, t.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    pt0_ice : array-like, deg C
        zero dbar (ITS-90)
        

    """
    return _gsw_ufuncs.pt0_from_t_ice(t, p)

@match_args_return
def pt_from_CT(SA, CT):
    """
    Calculates potential temperature (with a reference sea pressure of
    zero dbar) from Conservative Temperature.  This function uses 1.5
    iterations through a modified Newton-Raphson (N-R) iterative solution
    proceedure, starting from a rational-function-based initial condition
    for both pt and dCT_dpt.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    pt : array-like, deg C
        of zero dbar (ITS-90)
        

    """
    return _gsw_ufuncs.pt_from_ct(SA, CT)

@match_args_return
def pt_from_entropy(SA, entropy):
    """
    Calculates potential temperature with reference pressure p_ref = 0 dbar
    and with entropy as an input variable.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    entropy : array-like
        Specific entropy, J/(kg*K)

    Returns
    -------
    pt : array-like, deg C
        with reference sea pressure (p_ref) = 0 dbar.
        Note. The reference sea pressure of the output, pt, is zero dbar.
        

    """
    return _gsw_ufuncs.pt_from_entropy(SA, entropy)

@match_args_return
def pt_from_pot_enthalpy_ice(pot_enthalpy_ice):
    """
    Calculates the potential temperature of ice from the potential enthalpy
    of ice.  The reference sea pressure of both the potential temperature
    and the potential enthalpy is zero dbar.

    Parameters
    ----------
    pot_enthalpy_ice : array-like
        Potential enthalpy of ice, J/kg

    Returns
    -------
    pt0_ice : array-like, deg C
        

    """
    return _gsw_ufuncs.pt_from_pot_enthalpy_ice(pot_enthalpy_ice)

@match_args_return
def pt_from_pot_enthalpy_ice_poly(pot_enthalpy_ice):
    """
    Calculates the potential temperature of ice (whose reference sea
    pressure is zero dbar) from the potential enthalpy of ice.  This is a
    compuationally efficient polynomial fit to the potential enthalpy of
    ice.

    Parameters
    ----------
    pot_enthalpy_ice : array-like
        Potential enthalpy of ice, J/kg

    Returns
    -------
    pt0_ice : array-like, deg C
        

    """
    return _gsw_ufuncs.pt_from_pot_enthalpy_ice_poly(pot_enthalpy_ice)

@match_args_return
def pt_from_t(SA, t, p, p_ref):
    """
    Calculates potential temperature with the general reference pressure,
    p_ref, from in-situ temperature, t.  This function calls
    "gsw_entropy_part" which evaluates entropy except for the parts which
    are a function of Absolute Salinity alone.
    A faster gsw routine exists if p_ref is indeed zero dbar.  This routine
    is "gsw_pt0_from_t(SA,t,p)".

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    p_ref : array-like
        Reference pressure, dbar

    Returns
    -------
    pt : array-like, deg C
        ITS-90 temperature scale
        

    """
    return _gsw_ufuncs.pt_from_t(SA, t, p, p_ref)

@match_args_return
def pt_from_t_ice(t, p, p_ref):
    """
    Calculates potential temperature of ice Ih with the general reference
    pressure, p_ref, from in-situ temperature, t.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    p_ref : array-like
        Reference pressure, dbar

    Returns
    -------
    pt_ice : array-like, deg C
        p_ref, on the ITS-90 temperature scale
        

    """
    return _gsw_ufuncs.pt_from_t_ice(t, p, p_ref)

@match_args_return
def rho(SA, CT, p):
    """
    Calculates in-situ density from Absolute Salinity and Conservative
    Temperature, using the computationally-efficient expression for
    specific volume in terms of SA, CT and p  (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    rho : array-like, kg/m
        

    """
    return _gsw_ufuncs.rho(SA, CT, p)

@match_args_return
def rho_ice(t, p):
    """
    Calculates in-situ density of ice from in-situ temperature and pressure.
    Note that the output, rho_ice, is density, not density anomaly;  that
    is, 1000 kg/m^3 is not subracted from it.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    rho_ice : array-like, kg/m^3
        

    """
    return _gsw_ufuncs.rho_ice(t, p)

@match_args_return
def rho_t_exact(SA, t, p):
    """
    Calculates in-situ density of seawater from Absolute Salinity and
    in-situ temperature.  Note that the output, rho, is density,
    not density anomaly; that is, 1000 kg/m^3 is not subracted from it.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    rho_t_exact : array-like, kg/m^3
        

    """
    return _gsw_ufuncs.rho_t_exact(SA, t, p)

@match_args_return
def SA_freezing_from_CT(CT, p, saturation_fraction):
    """
    Calculates the Absolute Salinity of seawater at the freezing temperature.
    That is, the output is the Absolute Salinity of seawater, with
    Conservative Temperature CT, pressure p and the fraction
    saturation_fraction of dissolved air, that is in equilibrium
    with ice at the same in situ temperature and pressure.  If the input
    values are such that there is no positive value of Absolute Salinity for
    which seawater is frozen, the output, SA_freezing, is made a NaN.

    Parameters
    ----------
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    SA_freezing : array-like, g/kg
        given input values of its Conservative Temperature,
        pressure and air saturation fraction.
        

    """
    return _gsw_ufuncs.sa_freezing_from_ct(CT, p, saturation_fraction)

@match_args_return
def SA_freezing_from_CT_poly(CT, p, saturation_fraction):
    """
    Calculates the Absolute Salinity of seawater at the freezing temperature.
    That is, the output is the Absolute Salinity of seawater, with the
    fraction saturation_fraction of dissolved air, that is in equilibrium
    with ice at Conservative Temperature CT and pressure p.  If the input
    values are such that there is no positive value of Absolute Salinity for
    which seawater is frozen, the output, SA_freezing, is put equal to NaN.

    Parameters
    ----------
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    SA_freezing : array-like, g/kg
        given input values of Conservative Temperature
        pressure and air saturation fraction.
        

    """
    return _gsw_ufuncs.sa_freezing_from_ct_poly(CT, p, saturation_fraction)

@match_args_return
def SA_freezing_from_t(t, p, saturation_fraction):
    """
    Calculates the Absolute Salinity of seawater at the freezing temperature.
    That is, the output is the Absolute Salinity of seawater, with the
    fraction saturation_fraction of dissolved air, that is in equilibrium
    with ice at in-situ temperature t and pressure p.  If the input values
    are such that there is no positive value of Absolute Salinity for which
    seawater is frozen, the output, SA_freezing, is set to NaN.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    SA_freezing : array-like, g/kg
        given input values of in situ temperature, pressure and
        air saturation fraction.
        

    """
    return _gsw_ufuncs.sa_freezing_from_t(t, p, saturation_fraction)

@match_args_return
def SA_freezing_from_t_poly(t, p, saturation_fraction):
    """
    Calculates the Absolute Salinity of seawater at the freezing temperature.
    That is, the output is the Absolute Salinity of seawater, with the
    fraction saturation_fraction of dissolved air, that is in equilibrium
    with ice at in-situ temperature t and pressure p.  If the input values
    are such that there is no positive value of Absolute Salinity for which
    seawater is frozen, the output, SA_freezing, is put equal to NaN.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    SA_freezing : array-like, g/kg
        given input values of in situ temperature, pressure and
        air saturation fraction.
        

    """
    return _gsw_ufuncs.sa_freezing_from_t_poly(t, p, saturation_fraction)

@match_args_return
def SA_from_rho(rho, CT, p):
    """
    Calculates the Absolute Salinity of a seawater sample, for given values
    of its density, Conservative Temperature and sea pressure (in dbar).
    This function uses the computationally-efficient 75-term expression for
    specific volume in terms of SA, CT and p (Roquet et al., 2015).

    Parameters
    ----------
    rho : array-like
        Seawater density (not anomaly) in-situ, e.g., 1026 kg/m^3.
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    SA : array-like, g/kg
        Note. This is expressed on the Reference-Composition Salinity
        Scale of Millero et al. (2008).
        

    """
    return _gsw_ufuncs.sa_from_rho(rho, CT, p)

@match_args_return
def SA_from_SP(SP, p, lon, lat):
    """
    Calculates Absolute Salinity from Practical Salinity.  Since SP is
    non-negative by definition, this function changes any negative input
    values of SP to be zero.

    Parameters
    ----------
    SP : array-like
        Practical Salinity (PSS-78), unitless
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    SA : array-like, g/kg
        in_ocean  =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.sa_from_sp(SP, p, lon, lat)

@match_args_return
def SA_from_SP_Baltic(SP, lon, lat):
    """
    Calculates Absolute Salinity in the Baltic Sea, from Practical Salinity.
    Since SP is non-negative by definition, this function changes any
    negative input values of SP to be zero.
    Note. This programme will only produce Absolute Salinity values for the
    Baltic Sea.

    Parameters
    ----------
    SP : array-like
        Practical Salinity (PSS-78), unitless
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    SA_baltic : array-like, g kg^-1
        

    """
    return _gsw_ufuncs.sa_from_sp_baltic(SP, lon, lat)

@match_args_return
def SA_from_Sstar(Sstar, p, lon, lat):
    """
    Calculates Absolute Salinity from Preformed Salinity.

    Parameters
    ----------
    Sstar : array-like
        Preformed Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    SA : array-like, g/kg
        in_ocean  =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.sa_from_sstar(Sstar, p, lon, lat)

@match_args_return
def SAAR(p, lon, lat):
    """
    Calculates the Absolute Salinity Anomaly Ratio, SAAR, in the open ocean
    by spatially interpolating the global reference data set of SAAR to the
    location of the seawater sample.

    Parameters
    ----------
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    SAAR : array-like, unitless
        in_ocean  =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in or near the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.saar(p, lon, lat)

@match_args_return
def sigma0(SA, CT):
    """
    Calculates potential density anomaly with reference pressure of 0 dbar,
    this being this particular potential density minus 1000 kg/m^3.  This
    function has inputs of Absolute Salinity and Conservative Temperature.
    This function uses the computationally-efficient expression for
    specific volume in terms of SA, CT and p (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    sigma0 : array-like, kg/m^3
        respect to a reference pressure of 0 dbar,
        that is, this potential density - 1000 kg/m^3.
        

    """
    return _gsw_ufuncs.sigma0(SA, CT)

@match_args_return
def sigma1(SA, CT):
    """
    Calculates potential density anomaly with reference pressure of 1000
    dbar, this being this particular potential density minus 1000 kg/m^3.
    This function has inputs of Absolute Salinity and Conservative
    Temperature.  This function uses the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    sigma1 : array-like, kg/m^3
        respect to a reference pressure of 1000 dbar,
        that is, this potential density - 1000 kg/m^3.
        

    """
    return _gsw_ufuncs.sigma1(SA, CT)

@match_args_return
def sigma2(SA, CT):
    """
    Calculates potential density anomaly with reference pressure of 2000
    dbar, this being this particular potential density minus 1000 kg/m^3.
    Temperature.  This function uses the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    sigma2 : array-like, kg/m^3
        respect to a reference pressure of 2000 dbar,
        that is, this potential density - 1000 kg/m^3.
        

    """
    return _gsw_ufuncs.sigma2(SA, CT)

@match_args_return
def sigma3(SA, CT):
    """
    Calculates potential density anomaly with reference pressure of 3000
    dbar, this being this particular potential density minus 1000 kg/m^3.
    Temperature.  This function uses the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    sigma3 : array-like, kg/m^3
        respect to a reference pressure of 3000 dbar,
        that is, this potential density - 1000 kg/m^3.
        

    """
    return _gsw_ufuncs.sigma3(SA, CT)

@match_args_return
def sigma4(SA, CT):
    """
    Calculates potential density anomaly with reference pressure of 4000
    dbar, this being this particular potential density minus 1000 kg/m^3.
    Temperature.  This function uses the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    sigma4 : array-like, kg/m^3
        respect to a reference pressure of 4000 dbar,
        that is, this potential density - 1000 kg/m^3.
        

    """
    return _gsw_ufuncs.sigma4(SA, CT)

@match_args_return
def sound_speed(SA, CT, p):
    """
    Calculates the speed of sound in seawater.  This function has inputs of
    Absolute Salinity and Conservative Temperature.  This function uses the
    computationally-efficient expression for specific volume in terms of SA,
    CT and p (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    sound_speed : array-like, m/s
        

    """
    return _gsw_ufuncs.sound_speed(SA, CT, p)

@match_args_return
def sound_speed_ice(t, p):
    """
    Calculates the compression speed of sound in ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    sound_speed_ice : array-like, m/s
        

    """
    return _gsw_ufuncs.sound_speed_ice(t, p)

@match_args_return
def sound_speed_t_exact(SA, t, p):
    """
    Calculates the speed of sound in seawater.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    sound_speed_t_exact : array-like, m/s
        

    """
    return _gsw_ufuncs.sound_speed_t_exact(SA, t, p)

@match_args_return
def SP_from_C(C, t, p):
    """
    Calculates Practical Salinity, SP, from conductivity, C, primarily using
    the PSS-78 algorithm.  Note that the PSS-78 algorithm for Practical
    Salinity is only valid in the range 2 < SP < 42.  If the PSS-78
    algorithm produces a Practical Salinity that is less than 2 then the
    Practical Salinity is recalculated with a modified form of the Hill et
    al. (1986) formula.  The modification of the Hill et al. (1986)
    expression is to ensure that it is exactly consistent with PSS-78
    at SP = 2.  Note that the input values of conductivity need to be in
    units of mS/cm (not S/m).

    Parameters
    ----------
    C : array-like
        Conductivity, mS/cm
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    SP : array-like, unitless
        

    """
    return _gsw_ufuncs.sp_from_c(C, t, p)

@match_args_return
def SP_from_SA(SA, p, lon, lat):
    """
    Calculates Practical Salinity from Absolute Salinity.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    SP : array-like, unitless
        in_ocean  =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.sp_from_sa(SA, p, lon, lat)

@match_args_return
def SP_from_SA_Baltic(SA, lon, lat):
    """
    Calculates Practical Salinity for the Baltic Sea, from a value computed
    analytically from Absolute Salinity.
    Note. This programme will only produce Practical Salinty values for the
    Baltic Sea.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    SP_baltic : array-like, unitless
        

    """
    return _gsw_ufuncs.sp_from_sa_baltic(SA, lon, lat)

@match_args_return
def SP_from_SK(SK):
    """
    Calculates Practical Salinity from Knudsen Salinity.

    Parameters
    ----------
    SK : array-like
        Knudsen Salinity, ppt

    Returns
    -------
    SP : array-like, unitless
        

    """
    return _gsw_ufuncs.sp_from_sk(SK)

@match_args_return
def SP_from_SR(SR):
    """
    Calculates Practical Salinity from Reference Salinity.

    Parameters
    ----------
    SR : array-like
        Reference Salinity, g/kg

    Returns
    -------
    SP : array-like, unitless
        

    """
    return _gsw_ufuncs.sp_from_sr(SR)

@match_args_return
def SP_from_Sstar(Sstar, p, lon, lat):
    """
    Calculates Practical Salinity from Preformed Salinity.

    Parameters
    ----------
    Sstar : array-like
        Preformed Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    SP : array-like, unitless
        in_ocean  =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.sp_from_sstar(Sstar, p, lon, lat)

@match_args_return
def specvol(SA, CT, p):
    """
    Calculates specific volume from Absolute Salinity, Conservative
    Temperature and pressure, using the computationally-efficient 75-term
    polynomial expression for specific volume (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    specvol : array-like, m^3/kg
        

    """
    return _gsw_ufuncs.specvol(SA, CT, p)

@match_args_return
def specvol_anom_standard(SA, CT, p):
    """
    Calculates specific volume anomaly from Absolute Salinity, Conservative
    Temperature and pressure. It uses the computationally-efficient
    expression for specific volume as a function of SA, CT and p (Roquet
    et al., 2015).  The reference value to which the anomally is calculated
    has an Absolute Salinity of SSO and Conservative Temperature equal to
    0 degress C.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    specvol_anom : array-like, m^3/kg
        

    """
    return _gsw_ufuncs.specvol_anom_standard(SA, CT, p)

@match_args_return
def specvol_ice(t, p):
    """
    Calculates the specific volume of ice.

    Parameters
    ----------
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    specvol_ice : array-like, m^3/kg
        

    """
    return _gsw_ufuncs.specvol_ice(t, p)

@match_args_return
def specvol_SSO_0(p):
    """
    (no description available)
    """
    return _gsw_ufuncs.specvol_sso_0(p)

@match_args_return
def specvol_t_exact(SA, t, p):
    """
    Calculates the specific volume of seawater.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    specvol_t_exact : array-like, m^3/kg
        

    """
    return _gsw_ufuncs.specvol_t_exact(SA, t, p)

@match_args_return
def spiciness0(SA, CT):
    """
    Calculates spiciness from Absolute Salinity and Conservative
    Temperature at a pressure of 0 dbar, as described by McDougall and
    Krzysik (2015).  This routine is based on the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    spiciness0 : array-like, kg/m^3
        i.e. the surface
        

    """
    return _gsw_ufuncs.spiciness0(SA, CT)

@match_args_return
def spiciness1(SA, CT):
    """
    Calculates spiciness from Absolute Salinity and Conservative
    Temperature at a pressure of 1000 dbar, as described by McDougall and
    Krzysik (2015).  This routine is based on the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    spiciness1 : array-like, kg/m^3
        
        

    """
    return _gsw_ufuncs.spiciness1(SA, CT)

@match_args_return
def spiciness2(SA, CT):
    """
    Calculates spiciness from Absolute Salinity and Conservative
    Temperature at a pressure of 2000 dbar, as described by McDougall and
    Krzysik (2015).  This routine is based on the computationally-efficient
    expression for specific volume in terms of SA, CT and p (Roquet et al.,
    2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C

    Returns
    -------
    spiciness2 : array-like, kg/m^3
        
        

    """
    return _gsw_ufuncs.spiciness2(SA, CT)

@match_args_return
def SR_from_SP(SP):
    """
    Calculates Reference Salinity from Practical Salinity.

    Parameters
    ----------
    SP : array-like
        Practical Salinity (PSS-78), unitless

    Returns
    -------
    SR : array-like, g/kg
        

    """
    return _gsw_ufuncs.sr_from_sp(SP)

@match_args_return
def Sstar_from_SA(SA, p, lon, lat):
    """
    Converts Preformed Salinity from Absolute Salinity.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    Sstar : array-like, g/kg
        in_ocean  =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.sstar_from_sa(SA, p, lon, lat)

@match_args_return
def Sstar_from_SP(SP, p, lon, lat):
    """
    Calculates Preformed Salinity from Absolute Salinity.
    Since SP is non-negative by definition, this function changes any
    negative input values of SP to be zero.

    Parameters
    ----------
    SP : array-like
        Practical Salinity (PSS-78), unitless
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lon : array-like
        Longitude, -360 to 360 degrees
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    Sstar : array-like, g/kg
        in_ocean  =  0, if long and lat are a long way from the ocean
        =  1, if long and lat are in the ocean
        Note. This flag is only set when the observation is well and truly on
        dry land; often the warning flag is not set until one is several
        hundred kilometres inland from the coast.
        

    """
    return _gsw_ufuncs.sstar_from_sp(SP, p, lon, lat)

@match_args_return
def t_deriv_chem_potential_water_t_exact(SA, t, p):
    """
    Calculates the temperature derivative of the chemical potential of water
    in seawater so that it is valid at exactly SA = 0.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    t : array-like
        In-situ temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    chem_potential_water_dt : array-like, J g^-1 K^-1
        potential of water in seawater
        

    """
    return _gsw_ufuncs.t_deriv_chem_potential_water_t_exact(SA, t, p)

@match_args_return
def t_freezing(SA, p, saturation_fraction):
    """
    Calculates the in-situ temperature at which seawater freezes. The
    in-situ temperature freezing point is calculated from the exact
    in-situ freezing temperature which is found by a modified Newton-Raphson
    iteration (McDougall and Wotherspoon, 2013) of the equality of the
    chemical potentials of water in seawater and in ice.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    saturation_fraction : array-like
        Saturation fraction of dissolved air in seawater. (0..1)

    Returns
    -------
    t_freezing : array-like, deg C
        (ITS-90)
        

    """
    return _gsw_ufuncs.t_freezing(SA, p, saturation_fraction)

@match_args_return
def t_from_CT(SA, CT, p):
    """
    Calculates in-situ temperature from the Conservative Temperature of
    seawater.

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    t : array-like, deg C
        

    """
    return _gsw_ufuncs.t_from_ct(SA, CT, p)

@match_args_return
def t_from_pt0_ice(pt0_ice, p):
    """
    Calculates in-situ temperature from the potential temperature of ice Ih
    with reference pressure, p_ref, of 0 dbar (the surface), and the
    in-situ pressure.

    Parameters
    ----------
    pt0_ice : array-like
        Potential temperature of ice (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    t : array-like, deg C
        

    """
    return _gsw_ufuncs.t_from_pt0_ice(pt0_ice, p)

@match_args_return
def thermobaric(SA, CT, p):
    """
    Calculates the thermobaric coefficient of seawater with respect to
    Conservative Temperature.  This routine is based on the
    computationally-efficient expression for specific volume in terms of
    SA, CT and p (Roquet et al., 2015).

    Parameters
    ----------
    SA : array-like
        Absolute Salinity, g/kg
    CT : array-like
        Conservative Temperature (ITS-90), degrees C
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar

    Returns
    -------
    thermobaric : array-like, 1/(K Pa)
        respect to Conservative Temperature.
        Note. The pressure derivative is taken with respect to
        pressure in Pa not dbar.
        

    """
    return _gsw_ufuncs.thermobaric(SA, CT, p)

@match_args_return
def z_from_p(p, lat):
    """
    Calculates height from sea pressure using the computationally-efficient
    75-term expression for specific volume in terms of SA, CT and p
    (Roquet et al., 2015).  Dynamic height anomaly, geo_strf_dyn_height, if
    provided, must be computed with its p_ref = 0 (the surface).  Also if
    provided, sea_surface_geopotental is the geopotential at zero sea
    pressure. This function solves Eqn.(3.32.3) of IOC et al. (2010).

    Parameters
    ----------
    p : array-like
        Sea pressure (absolute pressure minus 10.1325 dbar), dbar
    lat : array-like
        Latitude, -90 to 90 degrees

    Returns
    -------
    z : array-like, m
        Note. At sea level z = 0, and since z (HEIGHT) is defined to be
        positive upwards, it follows that while z is positive in the
        atmosphere, it is NEGATIVE in the ocean.
        

    """
    return _gsw_ufuncs.z_from_p(p, lat)