# p32 完整准确前缀的终端残差与复核命令

[R287](../results/R287-actual-full-gap-stadium-H65-prefix-and-continuous-truncations.md)使用[低坡度新支持输入](2026-11-28-2ecf-stadium-full-gap-H65-slope-physical-inputs.md)真实 p32 ramp `00aa860c47894e81ecc5991b14cc446f380bceb903ab45e5e6bd0f3fb2568bc1` 和 Γ95 `978458636447335c6e00d542fdac538c5f27975b95ae92d56cc65d17ba6af502`。第零格入口准确支持函数分母可以含奇素数。程序在不少于 220 位的 dyadic 网格取最近系数，对每个所需导数按 $\sum |k|^j$ 加回逐系数确切有理舍入差。实部配对包括保存的 Nyquist 模。普通格、准确初格与修正末格各自覆盖闭原生角和闭径向区间。

## 终端法向导数的兼容多项式

用原生角 $\theta$，记 $p=\Gamma'$, $q=\Gamma''$, $E=p\cdot p$, $J=\sqrt E$, $H=|p\times q|$，$\lambda=f_0/a_\Gamma$。$T=p/J$，$N_F$ 和 $B_F$ 是正则空间曲线的 Frenet 法向、副法向。令 $V,A$ 是最后一个保存节点的原速度与加速度。准确 R137 速度 $d=bN_F+c_z B_F$，其中 $b=-vEJ/(a_\Gamma H)$，$c_z=\sqrt{1-b^2}$。程序先用整数 Fourier 乘法求实际小残差
$$
R_t=p\cdot V,\quad R_n=f_0[E(q\cdot V)-(p\cdot q)(p\cdot V)]+vE^2,\quad R_l=V^2-1.
$$
$V-d=\alpha T+\beta N_F+\gamma B_F$，有
$$
\alpha=R_t/J,\qquad \beta=\frac{R_n/f_0+v(1/a_\Gamma-1/f_0)E^2}{JH},\qquad
\gamma=\frac{R_l-\alpha^2-2b\beta-\beta^2}{V\cdot B_F+c_z}.
$$
最后一式使用 $V\cdot B_F>0$ 的逐盒证明。令 $N=d\times T$，$W_0=V\times p$，$W=d\times p=JN$。coast 的材料经线是测地线，$d_s$ 只有 $N$ 分量。其 Gauss 行列式准确为零，给出 $(d_s\cdot N)\lambda (q\cdot W)J=(d'\cdot W)^2$。于是 $A-d_s$ 在 $T,d,N$ 方向的误差由 $A\cdot p$, $A\cdot V$, 小差 $V-d$ 及多项式
$$
R_a=(A\cdot W_0)(q\cdot W_0)-(V'\cdot W_0)^2
$$
包出。法向分子 $\lambda(A\cdot W)(q\cdot W)-(d'\cdot W)^2$ 以 $R_a$、$\lambda-1$、$W_0-W$ 和 $V'-d'$ 展开后再区间求值。$q\cdot W$ 的正号全圈逐盒得到。最大乘积的完整 Fourier 次数是 1726；取低 192 频求区间，所有其余准确系数的绝对和及相应导数都加回。原端口比较量保留低 128 频及真实尾部。1024 个闭基盒共细分到 1652 叶，比较误差和真实高导数在同角 Taylor 算术中分别支付。

对于 $Y=P,d,d_s$，令 $o_j$ 为同角误差的 $j$ 阶界，$y_j$ 为真实 $Y^{(j)}$ 的范数界；$e_i$ 表示 $|\psi-\theta|,|\psi'-1|,|\psi''|$。合成后的零到二阶上界为
$$
o_0+y_1e_0,\quad o_1+y_2e_0+y_1e_1,\quad o_2+y_3e_0+y_2(2e_1+e_1^2)+y_1e_2.
$$
真实物理端口与普通谱端口的零、一、二阶角导数差矩阵逐项小于
$$\begin{pmatrix}
4.010\,10^{-11}&7.791\,10^{-9}&2.413\,10^{-6}\\
2.454\,10^{-8}&5.147\,10^{-6}&.001224\\
1.090\,10^{-5}&.282179&15562.47
\end{pmatrix}.$$
径格长度为二进结点的准确差 $L$，$\Delta_{ij}=\sum_{p=0}^2 L^{p-i}\|H_p^{(i)}\|_\infty d_{pj}$。即使 $d_{22}$ 很宽，它对空间角二阶 jet 的贡献仍有 $L^2\|H_2\|$ 因子，完整 $\Delta_{02}<.000239031$。在 $(s,u)$ 中，用原生真目标 $\rho^2 f^2$ 界估 $|X_u|$，仅在误差项使用 $1/\rho\le4$。全部交项保留后，非负入项绝对包络的最大特征值控制完整相对谱范数。用于主曲率计算的另一个较宽的纯原生 Gram $7.495\,10^{-6}$ 覆盖同一物理位置；相对度量使用独立更紧的材料 Gram $3.401002\,10^{-7}$。

## 复核

取 `S` 为本主题脚本目录，在空输出目录运行。先按前引输入和 [R283 回执](2026-11-28-2ecf-stadium-ruling-coast-reach-certificate.md)生成实际 p32 masters、源 JSON 与 `stadium-p32-coast-tight.json`。下列所有摘要均以本次重生文件相互校验。

```bash
p=stadium-p32r25-v012-H65
args=(--scripts "$S" --source "$p.json" --ramp "$p-ramp.npz" --coast "$p-coast.npz")
python "$S/2ecf-strong-stadium-terminal-speed-inverse.py" "${args[@]}" --cells 2048 --output speed.json
python "$S/2ecf-strong-stadium-terminal-speed-inverse.py" "${args[@]}" --cells 6144 --output speed-fine.json
python "$S/2ecf-strong-stadium-terminal-residual-trace.py" "${args[@]}" --inverse speed.json --output residual.json
python "$S/2ecf-strong-stadium-tight-terminal-composition.py" "${args[@]}" --inverse speed-fine.json --residual residual.json --output terminal.json
python "$S/2ecf-strong-stadium-native-ramp-gram.py" "${args[@]}" --left 0 --right 1 --kcap 8 --output first.json
python "$S/2ecf-strong-stadium-native-ramp-gram.py" "${args[@]}" --left 1 --right 64 --kcap 9.2 --output middle.json
python "$S/2ecf-strong-stadium-native-ramp-gram.py" "${args[@]}" --left 63 --right 64 --kcap 9.2 --end-trace terminal.json --output last.json
python "$S/2ecf-strong-stadium-exact-radial-witness.py" --scripts "$S" --source "$p.json" --ramp "$p-ramp.npz" --output witness.json
python "$S/2ecf-strong-stadium-accurate-whole-prefix.py" "${args[@]}" --first first.json --middle middle.json --terminal last.json --tight terminal.json --ruling stadium-p32-coast-tight.json --output whole.json
```

准确高次乘积助手为 `2ecf-strong-stadium-terminal-algebra.py`。时间字段会使重生 JSON 的整文件摘要变化；有理界、覆盖、见证和可重复的叶摘要由实际程序输出。原运行的首、中、末格和全域消费回执 SHA-256 分别为 `e85518aadc54db5d0e8b91ddb93bbf453e2bb58ed7423ebebad09ead97e7af51`、`10a1e43b9cd1c748712b33b231a98dc5b32d3f9fc938b1365ff0aa68e2688cb3`、`63f60ee5dcf5691d3fbf7076bfbb526ab8694ed87b990df652ccc53d55986131`、`5d8bdd8a0e95d3c16362b0cf70582fe1fec4effa81d0fd1d1ad2d5e6cc18a79f`。

普通格命令额外算出原始未修正的第 63 格，仅作代理记录。最后消费者显式只读其中第 1 至 62 格，另取真实修正右端口的最后格。可在同一个复核目录使用 `--right 63` 跳过这项非必需的代理。
