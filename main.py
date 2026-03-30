import argparse
from code.Natural_Response import simulate_rlc as simulate_natural, plot_results as plot_natural
from code.Forced_Response import simulate_rlc as simulate_forced, plot_results as plot_forced


def main():
    parser = argparse.ArgumentParser(description="RLC Circuit Simulator")

    parser.add_argument("--mode", choices=["natural", "forced"], required=True)
    parser.add_argument("--R", nargs="+", type=float, required=True)
    parser.add_argument("--L", type=float, default=1.0)
    parser.add_argument("--C", type=float, default=1.0)
    parser.add_argument("--V_in", type=float, default=1.0)

    args = parser.parse_args()

    t_span = (0, 10)

    if args.mode == "natural":
        x0 = [1, 0]
        results = simulate_natural(args.R, args.L, args.C, t_span, x0)
        plot_natural(results)

    elif args.mode == "forced":
        x0 = [0, 0]
        results = simulate_forced(args.R, args.L, args.C, args.V_in, t_span, x0)
        plot_forced(results)


if __name__ == "__main__":
    main()