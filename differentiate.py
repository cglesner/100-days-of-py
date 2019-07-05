"""implement a function derivative."""
import func

def d_dx(f):
    """Diferentiate a Pterm, f with respect to it's input variable, x."""
    assert isinstance(f, func.Pterm), "Input must be of type func.Pterm."

    # Grab current terms.
    c_old, p_old = f.c, f.p

    # Calculate new terms.
    p_new = p_old - 1 if p_old != 0 else 0
    c_new = c_old*p_old

    # Construct a new func.Pterm object.
    return func.Pterm((p_new, c_new))