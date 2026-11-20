# R939 新素数窗口与权 34 固定 σ 系数的公开回执

2026-11-20，serre-public-astra-20261120-de0a3e3b。仅记录本次公开 Actions 的参数、来源、结论与哈希；完整可再生数组不入库。

公开 [run 44716895805](https://github.com/Rogerhu12/math-research-public/actions/runs/44716895805)，job `136222480093`，source `7843407c2633ffd5f9041a137bd9fe7174021b65`，2026-11-20 10:12:26 UTC 完成，结论 `success`。workflow 为 `.github/workflows/serre-current-exact-research.yml`，执行前核对两 README 及每个脚本的完整 SHA256。临时 JSON 只在 runner `/tmp` 中生成，没有 artifact 或 Release 上传。本地没有执行数学计算。

## 1. 完整原超奇异点和的新窗口

脚本 `scripts/R939_trace_window.py`，SHA256 `f84ebe39808e9a07903ea95131c9c9b4b19cc76fdcb77225d94278833604c1a6`；参数 `--minimum 109 --maximum 1000 --output /tmp/R939-window.json`。实际取原允许类 $p\equiv5\pmod6$、$p\equiv2,5\pmod9$；六个旧 R936 素数不重复。

本次完整覆盖 48 个新素数，最后为 983，没有完整和 $S$ 为零的素数。对每个新素数同时验证：原 Hasse 的全多项式微分方程、$\beta'=-H/3$、整个 $tH$ 代数中的 $\beta=b$ 与 $\beta^p=\beta$、$\beta^{p-1}=1$、原分母表达与新无分母表达逐项相同、两种独立 trace 相同、全部点权及椭圆点零贡献。$r=2$ 行还验证原伴随 $C$ 的微分方程右侧为 $-sH/9$。

确定性临时输出 54,494 bytes，SHA256 `900524ddf9b53e831ec32e9a64a2bc9c394a22a738574877ce6b872d5209d2ab`。逐行原来源哈希可从公开日志或脚本重现；不把整窗数组提交到仓库。

这只是一段有限窗及原来源恒等式的核验。它没有证明所有充分大的 $p$ 都非零，也没有给出该完整和与原 $Q'_h(0)$ 的高层来源比较。

## 2. 原权 34 顶配对所需的固定系数

脚本 `scripts/weight34_sigma_top.py`，SHA256 `053dc98d70ce13f980f9f35ae98c837dca866c72bf348feab98d98c10b2de7e9`；参数 `--output /tmp/weight34-sigma-top.json`。保持原曲线 $y^2=x^3-1$、$dz=dx/(2y)$、$(\log\sigma)''=-x$、$\sigma=z+O(z^7)$、$c=0$。

在 $x\sigma^6=z^4\sum f_i z^{6i}$ 中准确得到
$$
f_5=-\frac{270862728}{5123589312701234375},\qquad
270862728=2^3\cdot3\cdot41\cdot71\cdot3877.
$$
分母的完整分解为 $5^6 7^4 11^2 13^2\cdot17\cdot19\cdot23\cdot29\cdot31$。故 $p\ge41$ 时 $f_5$ 为单位的例外恰在固定集合 $\{41,71,3877\}$，不是对所有 $p$ 的单位声明。

原 R697 标度给
$$
A_{35}=-119077474393745219911680,\qquad
C_{35}=\frac{789548077693836634073616}{5479774665990625}.
$$
旧 $f_0,f_1,f_2$ 只作归一一致性检查；$Y^2=X^3-t$ 的独立能量恒等式和原平方标度也通过。确定性输出 SHA256 `1fe703b1d888d361161aba47492091e45b9442357d31c1e430dda04614165a65`。

这关闭了固定 $f_5$ 常数本身的待算项；原权 34 的 $a_h$、两 CM 权、Norm、相位、同标签临界积及低 $Q'_h(0)$ 仍按各自来源保留。已登记的 $p=41$ 模零不重做。
