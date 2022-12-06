def plot_disp(ax, tws, top_plot, font_size):
    S = [p.s for p in tws]#map(lambda p:p.s, tws)
    d_Ftop = []
    Fmin = []
    Fmax = []
    for elem in top_plot:
        Ftop = [p.__dict__[elem] for p in tws]

        Fmin.append(min(Ftop))
        Fmax.append(max(Ftop))
        greek = ""
        if "beta" in elem or "alpha" in elem or "mu" in elem:
            greek = "\\"
        if "mu" in elem:
            elem = elem.replace("mu", "mu_")
        top_label = r"$" + greek + elem+"$"
        ax.plot(S, Ftop, lw = 2, label=top_label)
        d_Ftop.append( max(Ftop) - min(Ftop))
    d_F = max(d_Ftop)
    if d_F == 0:
        d_Dx = 1
        ax.set_ylim(( min(Fmin)-d_Dx*0.1, max(Fmax)+d_Dx*0.1))
    if top_plot[0] == "E":
        top_ylabel = r"$"+"/".join(top_plot) +"$"+ ", [GeV]"
    elif top_plot[0] in ["mux", 'muy']:
        top_ylabel = r"$" + "/".join(top_plot) + "$" + ", [rad]"
    else:
        top_ylabel = r"$"+"/".join(top_plot) +"$"+ ", [m]"

    yticks = ax.get_yticks()
    yticks = yticks[2::2]
    ax.set_yticks(yticks)

    ax.set_ylabel(top_ylabel, fontsize=font_size)
    ax.tick_params(axis='both', labelsize=font_size)

    leg2 = ax.legend(loc='upper right', shadow=False, fancybox=True, prop=font_manager.FontProperties(size=font_size))
    leg2.get_frame().set_alpha(0.2)