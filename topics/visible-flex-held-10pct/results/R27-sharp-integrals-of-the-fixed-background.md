# R27. 同一固定背景的真积分精细区间

会话：Astra-held10-7322d0de-20261118；共同工作 `closed_geometry`。2026-11-17 UTC（2026-11-18 UTC+8）。

## 结论与范围

对 R21、R23、R24 及既有同 g M8/M16 比较使用的**同一个固定旋转背景**，真实归一化常数满足

\[
 \frac{1423832416729385}{8796093022208}
 \le \lambda \le
 \frac{5695329666917957}{35184372088832}.
\]

两端显示为 $161.87100490348996$ 与 $161.8710049035018$。背景真实高度满足

\[
 \frac{6497083433548809}{288230376151711744}
 \le h(r_{\rm cut}) \le
 \frac{1624270858389905}{72057594037927936},
\]

显示为 $[.022541286315114237,.022541286315151746]$。下表使用进一步向外放宽的十进制数，因而可直接按十进制有理数理解。

| 真实量 | 下界 | 上界 |
|---|---:|---:|
| $\int A$ | .1527498791689533 | .1527498791689535 |
| $\int B$ | .0006007877747408902 | .0006007877747409341 |
| $\int wA$ | .0193119724963948 | .0193119724963949 |
| $\int wB$ | .00001994992136266002 | .00001994992136289024 |
| cell0 的内半径 | .1357157623768878 | .1357157623768922 |

这是 R21 粗区间的精度推进，未重新设计物理参数，未重新求解非线性 BVP。固定的 binary64 校准常数和原参数文件不变。该结果只认证上述真实积分和归一化；它本身不是非旋转闭图的连续 metric 证书。

## 1. 固定定义与输入

沿用 R21 的定义，原每段参数为 $x\in[0,1]$，$r_o$ 为未重新分配的径向变量，$w>0$，$E=1+w^2$，正权重为 $W$：

\[
 A=(1-\chi)j_0(r_o)_x+\chi\frac{|w_x|}{8E^{3/2}},
 \qquad B=\chi\frac{(r_o)_x}{E}W,
 \qquad r_x=A+\lambda B,
\]

\[
 \lambda=\frac{r_{\rm cut}-r_{160}-\int A}{\int B},
 \qquad h(r)=\int_a^r w(v)\,dv.
\]

有限的 160 个 cell 的校准常数按 R21 的规定取已冻结 binary64 数，之后按精确有理数解释。$r_{\rm cut}=.3$、$w_{\rm cut}=.08$、曲率预算 8、protectCell=160、$\delta_0=.006$ 等均未变化。特别地，前六个 valley controls 仍是

\[
 (3.125,2.8125,4.0625,5,5.25,4.0625),
\]

其后为零；本结果不自动覆盖改变这些参数的新背景。

输入 `m3_fixed_background_constants.json` 的 SHA-256 为
`f9efb5c41fc7a4e683222c86bce279d94fc5f328332c6ff21db82901a864fab9`。
它由 R21 的 `dump_background_constants.mjs` 从原 M8 tail checkpoint
`12754098ba6cffc0abb5f0c327c7a376cac826ea8ab820b793ec5ad9b958c4f2`
恢复；源依赖及原背景定义仍是 R21 的固定来源。参数中的模数和离散步数不进入这里的真实积分定义。

## 2. 普通段的两个总变差恒等式

前 48 个 cell 中，除了 cell0 的第8段（从0计数），都有 $\chi=1$。定义

\[
 U(w)=\frac{w}{\sqrt{1+w^2}},\qquad
 V(w)=-\frac1{\sqrt{1+w^2}}.
\]

直接微分得到

\[
 U'(w)=E^{-3/2},\qquad V'(w)=wE^{-3/2}.
\]

由于 $w>0$，对任意参数子区间 $I$ 都有

\[
 \int_I A\,dx=\frac18\operatorname{TV}_I(U\circ w),
 \qquad
 \int_I wA\,dx=\frac18\operatorname{TV}_I(V\circ w).
\]

若整个 $I=[l,r]$ 上的区间导数证明 $w_x\ge0$，这两个积分分别等于

\[
 \frac{U(w(r))-U(w(l))}{8},\qquad
 \frac{V(w(r))-V(w(l))}{8}.
\]

若证明 $w_x\le0$，则交换端点。端点函数全部用外向区间初等函数求值。这里没有把数值求得的 critical point 当成精确分界。

如果导数区间跨零，直接采用完整值域界

\[
 0\le\int_I A\,dx
 \le |I|\sup_I\frac{|w_x|}{8(1+w^2)^{3/2}},
 \qquad
 0\le\int_I wA\,dx\le (\sup_I w)\,\overline{A}_I,
\]

并继续自适应二分。因此不论真正的 turning point 位于区间何处、是否位于端点，覆盖都成立。对平帽段 $w_x=0$，总变差公式也直接成立。

## 3. $B,wB$ 的严格 Simpson 余项

每个原九段 cell 内的 log-profile、权重和 $r_o$ 都由已冻结常数、指数函数与五次 smoothstep 构成。对 cap 过渡设

\[
 t=\frac{z-c+L}{2L},\qquad
 I(t)=t-7t^5+14t^6-10t^7+\frac52t^8,
\]

其中 $z=\log w_{\rm raw}$，$c$ 为局部 cap 的对数，$L=2$。实际 cap 是三段函数：

\[
 z\quad(z-c\le-L),\qquad
 c-L+2LI(t)\quad(|z-c|\le L),\qquad
 c\quad(z-c\ge L).
\]

$I'(t)=1-S_7(t)$，而 $S_7$ 在0、1的前3阶导数为零，故这些分支的0至4阶导数相接。局部 cap $c(x)$ 可变时也成立。因此所需的 $B,wB$ 在每个原段内部是 $C^4$，可以在跨 cap 分界的子区间上使用四阶余项；不要求相邻的原九段在更高阶相接。

对 $f=B$ 或 $wB$，令 $d=r-l$、$m=(l+r)/2$。Simpson 公式为

\[
 Q_I(f)=\frac d6(f(l)+4f(m)+f(r)),
\]

且

\[
 \left|\int_I f-Q_I(f)\right|
 \le\frac{d^5}{2880}\sup_I|f^{(4)}|
 =\frac{d^5}{120}\sup_I|f^{[4]}|,
\]

其中 $f^{[4]}=f^{(4)}/4!$。源码在整个 $I$ 上用4阶区间 Taylor jet 计算 $f^{[4]}$。加法、卷积乘法、倒数、平方根和指数的 Taylor 递推都只作外向区间运算；分母非零及平方根正性逐次检查。由运算递推的链式法则，所得每一阶区间包含整个子区间上的相应真实导数。

跨 cap 分界时分别计算所有可能分支，再逐阶取凸包。过渡分支将 $t$ 的**值域**与 $[0,1]$ 相交，同时保留 $t(x)$ 的全部导数区间；这只是对该分支定义域的限制，没有把截断函数求导。为了避免符号消去掩盖导数符号，还使用等价公式

\[
 I'(t)=(1-t)^4(1+4t+10t^2+20t^3)\in[0,1],
\]

\[
 (\operatorname{cap}z)_x=I'(t)z_x+(1-I'(t))c_x.
\]

五次 smoothstep 的值域和一阶导数值域利用
$S_5' =30x^2(1-x)^2\ge0$ 及唯一最大点 $x=1/2$ 收紧。其余 jet 项仍使用完整区间，故这些改写不会删去真实导数。

cell0 的第8段单独处理：这里不启用 cap，$w_x=-\kappa w$，$\kappa=7\ell/\sqrt{12}>0$，$\ell$ 为该原段长度。令 $S=S_5(x)$，则

\[
 A=(r_o)_xj_0S+(1-S)\frac{\kappa w}{8E^{3/2}}.
\]

这是不含绝对值折点的光滑式，$A,wA,B,wB$ 四个积分均可用上述严格 Simpson 余项。protect160 的另一特殊段不在前48个 cell 内，由下一节的余项一起覆盖。

## 4. 深处余项与真正归一化

R21 已给出的深处估计仍适用。取 $N=48$，定义

\[
 W_N=256\,2^{-7N/4},\quad H_N=17+7N/5,\quad q=3/10>2^{-7/4}.
\]

所有未逐段积分的 cell 的总变差可由

\[
 T_N=W_N\left(\frac{4H_N+1}{1-q}
 +\frac{(28/5)q}{(1-q)^2}\right)
\]

控制。令

\[
 Y_N=6\delta_0 2^{-N}
 +\frac{6\eta_0 2^{-3N/2}}{1-2^{-3/2}},\qquad
 R_N=a\bigl(e^{Y_N/\sqrt{12}}-1\bigr),
\]

则可分别给 $A,B,wA,wB$ 的积分加上非负余项

\[
 T_N/8+R_N,\quad R_N,\quad
 W_N(T_N/8+R_N),\quad W_NR_N.
\]

本次四个余项上界依次为
$1.846849\times10^{-18}$、$1.846045\times10^{-18}$、
$2.444284\times10^{-41}$、$2.443220\times10^{-41}$。
protect160 的混合径向项由这里的 $R_N$ 覆盖。深于160的原背景高度另外加上

\[
 256\,2^{-280}a\bigl(e^{Y_{160}/\sqrt{12}}-1\bigr).
\]

于是对四个完整积分作外向区间求和，再代入

\[
 \lambda=(r_{\rm cut}-r_{160}-\mathcal A)/\mathcal B,
 \qquad h(r_{\rm cut})=\mathcal A_H+\lambda\mathcal B_H+h_{\rm deep},
\]

便得到开头的区间。$\mathcal B>0$、$\lambda>0$ 在本次计算中直接由严格下端点验证。cell0 内半径同样由去掉 cell0 后的真实积分与同一个 $\lambda$ 得到。

## 5. 算术、实际执行与复现

新源码为 [certify_background_sharp.py](../scripts/resume_closed/certify_background_sharp.py)。区间初等函数使用60位 `mpmath.iv`；普通高精度标量使用90位，所有 binary64 输入先转为 `Fraction.from_float` 的精确有理数。二分区间不允许深于128层，故参数端点、差、和及 Simpson 中点在该精度下精确。该硬门不通过时程序必须停止，不会用近似中点宣称严格余项。

优先队列只决定先分哪一个区间。是否达到每原段 $10^{-17}$ 的宽度目标，以**全部当前叶区间的外向求和**判断；不依靠相邻 quadrature 结果的差，也不依靠有抵消的误差估计。实际共积分48个 cell、432个原段，使用10,034个叶区间，最大二分深度32。完整执行参数、源与输入输出 SHA-256 见 [background_sharp_execution.json](../scripts/resume_closed/background_sharp_execution.json)。大区间输出在运行时生成，不入仓库。

先按 R21 的来源恢复 `SOURCE`，使用其 `dump_background_constants.mjs` 导出相同固定输入，然后执行：

```bash
python topics/visible-flex-held-10pct/scripts/resume_closed/certify_background_sharp.py \
  --input SCRATCH/background-constants.json \
  --cells 48 --piece-width 1e-17 \
  --out SCRATCH/background-sharp.json
```

源路径等非数学元数据改变可以改变 JSON 字节哈希；必须同时核对冻结 checkpoint、160个校准常数及物理参数，不能仅比较一个路径相关的文件哈希。

## 6. 数值工厂与连续 metric 的剩余区别

原数值工厂给出的 binary64 归一化值是 $161.87100490352205$。把它也按精确 binary64 有理数解释，本证书证明

\[
 2.0236\times10^{-11}
 <\lambda_{\rm factory}-\lambda
 <3.2089\times10^{-11}.
\]

因此，工厂点查询的归一化常数不能字面替换本课题固定的真积分常数，即使其差很小。原数值高度 $.02254128631512652$ 落在本次真实高度区间内。较粗的每段 $10^{-13}$ 运行给出的 $\lambda$ 宽区间包含工厂值；加精后才分辨出上述严格非零差。

本证书不把归一化精度自动解释成全半径上的 $w(r)$ 点查询误差界。后者仍须支付各段部分积分、反函数以及有限非旋转 Fourier 图的连续径向误差；把这些界组合后才能认证整个固定 g 的 metric。已证明的 C²、嵌入、reach 和固定标记结论不依赖把该数值工厂值当成精确常数。
