# R812 — 原同 charge 抵消、两来源角格与完整 carry 预算

日期：2026-11-15。**状态：已证明。**

令 $A(z)=S(2z)/64$，$B(z)=U_{136}(z)-A(z)$。本篇给出完整倍点多项式、原点和全部固定角除子、原中央的精确线性运输，以及新两生成元格 $\mathbf Z[S,B]$ 的全次数预算。确有
$$
B=w^2(1890+O(w)),\qquad w=z^6,
$$
但其 Gaussian charge 仍为四，原 $d=1+8t$ 极没有降低。

结论分清两个格。在原 canonical 来源中已包含 $A$ 时，以 $B=U-A$ 替换附加的 $U$ 是同 charge 的可逆整列变换，保每一个实际前缀、全部精度、原 $P_{134}/U_0$ 和十三行 carry。独立选用 $\mathbf Z[S,B]$ 则是合法的、不同的来源格：原点链改变，但完整 canonical 成员锥仍恰为 $i\ge4j$；现有复、普通及惰性预算主项没有严格改善。纯起阶收益在全旗标中只有 $O(D^3\log D)$，不能替代原 $D^4\log D$ 主预算。

没有把 $B$ 的来源系数、较高原点阶、规范化或乘积赋予新的中央零。原 $S/U$ 两中央条件对该新格的更强实际惰性约束仍需独立证明。

## 1. 完整倍点来源

使用 R468 的共同 $b=1$ 模型
$$
y^2=x^3+1,\quad X=x^3,\quad t=-X^{-1},\quad
\Theta=x\sigma^2,\quad d=1+8t,\quad h_7=7+4t+16t^2,
$$
$$
a=t(t-1)h_7,\qquad
S=\Theta^{17}ad/7,\qquad U=\Theta^{68}aH_{18}/91.
\tag{1}
$$
$U$ 是 R466/R469 的原 $E_{2312}$ 来源，首 $z^6$ 系数为一。固定多项式为
$$
\begin{aligned}
H_{18}={}&(8t^2+20t-1)\\
&\cdot(256t^4-1024t^3+1536t^2-52t+13)\\
&\cdot(1792t^4-3136t^3+2112t^2-40t+1)\\
&\cdot(32768t^8-851968t^7+1949696t^6-2111488t^5\\
&\hspace{16mm}+439040t^4-49408t^3+58688t^2+1232t-1).
\end{aligned}
\tag{2}
$$
在原 $D_zx=2y$ 规范中，
$$
\sigma(2z)=-2y\sigma^4,\quad
x(2z)=\frac{x(X-8)}{4(X+1)},\quad
X(2z)=\frac{X(X-8)^3}{64(X+1)^3}.
\tag{3}
$$
置
$$
\begin{aligned}
A_2&=X^2+20X-8,& B_4&=X(X-8)^3-512(X+1)^3,\\
H_2&=7X^2-4X+16,\\
R_6&=X^6-84X^5+11040X^4+47936X^3
 +204288X^2+33792X+4096.
\end{aligned}
\tag{4}
$$
由 (3) 得
$$
X(2z)+1=\frac{A_2^2}{64(X+1)^3},\qquad
X(2z)-X=-\frac{9X(X+4)H_2}{64(X+1)^3},
$$
$$
7X^2(X-8)^6-256X(X-8)^3(X+1)^3+65536(X+1)^6=H_2R_6.
\tag{5}
$$
最后一式也可按
$$
R_6=4096(X+1)^6
-9X(X+4)\{7X(X-8)^3+64(7X-4)(X+1)^3\}
$$
直接核定。代入原 $S=\sigma^{34}x^2(X+1)(X-8)H_2/7$，
$$
\boxed{
A=\frac{S(2z)}{64}
=\frac{\sigma^{136}x^2}{7}
 (X+1)^3(X-8)^2 A_2^2 B_4 H_2R_6.
}
\tag{6}
$$
全部因子均保留，特别不能省去 $B_4$。

定义
$$
\begin{aligned}
A_t&=1-20t-8t^2,\\
B_t&=1+536t-1344t^2+2048t^3-512t^4,\\
R_t&=t^6R_6(-1/t),\\
H_{16}&=(t-1)^2A_t^2B_tR_t.
\end{aligned}
\tag{7}
$$
则 $\deg H_{16}=16$、$H_{16}(0)=1$，完整角式为
$$
\boxed{A=\Theta^{68}ad^2H_{16}/7.}
\tag{8}
$$
一般固定 $b$ 由原齐次缩放恢复。本篇全局格在共同 $b=1$ 模型计算，回原模型只用 R468/R469 已付的固定代数周期运输。

## 2. 抵消后的全部角阶与真实二生成元域

令
$$
K_{17}=\frac{H_{18}-13d^2H_{16}}t.
\tag{9}
$$
分子常数恰为零，$\deg K_{17}=17$，且
$$
\boxed{B=\Theta^{68}atK_{17}/91.}
\tag{10}
$$
完整多项式除法给
$$
K_{17}(0)=-24570,\quad K_{17}(1)=-3^{27},\quad
K_{17}(-1/8)=3^{27}/2^{17},\quad \gcd(K_{17},ad)=1.
\tag{11}
$$
准确角阶为
$$
\begin{array}{c|ccccc}
&t=0&t=1&h_7=0&d=0&\deg_t\\ \hline
A/\Theta^{68}&1&3&1&2&22\\
U/\Theta^{68}&1&1&1&0&22\\
B/\Theta^{68}&2&1&1&0&22 .
\end{array}
\tag{12}
$$
$h_7=0$ 一栏对两个根逐个成立；$A_t$ 在 $B/\Theta^{68}$ 中恰一次。没有新增 $h_7$、$t-1$ 或 $d$ 因子。若需把全部角阶同时约化到剩余域，可再删固定 resultant 的有限素因子，不增加随深度变化的坏集。

由 $a=-7t+O(t^2)$、$t=-w+O(w^2)$，
$$
\boxed{B=1890w^2+O(w^3),\qquad1890=2\cdot3^3\cdot5\cdot7.}
\tag{13}
$$
在好素数 $p>83$ 上首项为单位。可固定改用 $B/1890$，但下文保原常数。

两来源 $S,B$ 代数独立，因为
$$
\boxed{
\frac B{S^4}=\frac{343}{13}
\frac{K_{17}}{t^2(t-1)^3h_7^3d^4}.
}
\tag{14}
$$
分子次数十七、分母次数十五且互素，故为次数十七的非恒定有理映射。R418 已证明 $t,\Theta$ 代数独立；(14) 使 $t$ 代数于 $\mathbf Q(S,B)$，而 $\Theta^{17}=7S/(ad)$。因此二者的超越次数恰为二。

若 $q=\Theta^{17}$，更准确地
$$
[\mathbf Q(t,q):\mathbf Q(S,B)]=17.
\tag{15}
$$
不能把整个 $q^n$ 角多项式空间当作 $\mathbf Q[S,B]$；那会无证加入十七次覆盖的其它来源。真实格计数始终保此区别。

## 3. 原中央的准确运输及完整 Gaussian

普通处使用原共同周期和同一有界测度：
$$
\nu_A=64^{-1}[2]_*\nu_S,\qquad
M_A(v)=64^{-1}\langle2\rangle^{(p-1)v}M_S(v).
\tag{16}
$$
原单位质量 $M_S(0)=0$，故
$$
M_B'(0)=M_U'(0)-M_S'(0)/64.
\tag{17}
$$
两个原中央同时零确实给 $S,B$ 的中央零，未传播到 $S^iB^j$。

惰性处令 $p=6s-1>83$，保 R468 全规范
$$
\kappa=34c_p+\Delta,\qquad a_p=p\kappa\in\mathcal O^\times,\qquad
g=d\Theta^{17}e^{-\kappa w^s}.
\tag{18}
$$
$A,U,B$ charge 都为四。置
$$
q_p(2)=\frac{2^{p-1}-1}{p},\quad
\rho_p^{(2)}=64^s=4(1+pq_p(2)),\quad
\varepsilon_p=(\rho_p^{(2)}-4)\kappa=4a_pq_p(2).
$$
$\varepsilon_p$ 整，但不假设为单位。全部来源式为
$$
\boxed{\widehat A=64^{-1}e^{\varepsilon_pw^s}\widehat S(64w),
\qquad \widehat B=(g/d)^4atK_{17}/91.}
\tag{19}
$$
若 $c_{S,j}=[w^{js}]\widehat S$，每个 $j\ge0$ 都有
$$
c_{A,j}=\frac1{64}\sum_{h=0}^j
\frac{\varepsilon_p^h}{h!}(\rho_p^{(2)})^{j-h}c_{S,j-h},
\qquad c_{S,0}=0.
\tag{20}
$$
R314 的完整 Newton 恒等式给
$$
J_A(v)=64^{-1}(2^{p-1})^vJ_S(v),\qquad
J_B'(0)=J_U'(0)-J_S'(0)/64.
\tag{21}
$$
这保整个高尾，不是仅前三权。

对 R468 的单位归一
$$
F_\nu=c_{\nu,1}/q_\nu-\frac p{q_\nu^2a_p}c_{\nu,2}
+\frac{2p^2}{q_\nu^3a_p^2}c_{\nu,3},
$$
取 $q_A=q_B=q_U=4,q_S=1$，有
$$
\boxed{F_A=F_S/64\pmod{p^3},\qquad
F_B=F_U-F_S/64\pmod{p^3}.}
\tag{22}
$$
例如令 $r=1+pq_p(2)$，$c_{S,1}$ 的系数括号为
$r(1-pq_p(2)+p^2q_p(2)^2)=1\bmod p^3$；另两项分别为
$-p/a_p,2p^2/a_p^2\bmod p^3$。全部下一位 $q_p(2)$ carry 因此按 (20) 精确保留，未先删除。

(19)–(22) 是实际来源的分布关系。对 R468 人为改变高角系数的计算族，不能逐参数无证认同倍点身份；也没有从它增加第四条独立算术中央条件。

## 4. 新格的分级及准确 canonical 成员锥

令 $n=i+4j$、$\mathscr R=d\Theta^{17}$。全部实际单项式是
$$
\boxed{
S^iB^j=
\frac{\mathscr R^n}{7^i91^j}
\frac{t^{i+2j}(t-1)^{i+j}h_7^{i+j}K_{17}^j}{d^{4j}}.
}
\tag{23}
$$
其原点阶为 $i+2j$，首项 $1890^j$。固定 charge $n$ 时取 $i=n-4j$，这些阶恰为各不相同的 $n-2j$。原 $S^iU^j$ 则为 $n-3j$：原点链确由步长三变成步长二，Gaussian charge 仍为 $n$。

R365 的原格为
$$
\mathcal V_n=\mathscr R^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\quad
q_n=\frac{(th_7)^{\alpha_n}(t-1)^{\beta_n}}{d^{\gamma_n}},
$$
$$
\alpha_n=\lfloor(n+1)/4\rfloor,\quad
\beta_n=\lfloor(n+1)/3\rfloor,\quad
\gamma_n=\lfloor n/2\rfloor,\quad
\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4.
\tag{24}
$$
(23) 除以 $q_n$ 的四个固定指数为
$$
\begin{array}{c|c}
t&i+2j-\alpha_n\\
h_7&i+j-\alpha_n\\
t-1&i+j-\beta_n\\
d&\lfloor i/2\rfloor-2j .
\end{array}
\tag{25}
$$
前两项总非负。由 (11)，负 $d$ 阶不能被 $K_{17}$ 取消，故必要条件是 $i\ge4j$。该条件下 $t-1$ 阶亦非负。完整相对角有理函数的无穷次数是 $4i+18j$，canonical 帽则为
$4i+18j+\lfloor i/2\rfloor+4$，故所有无穷条件也成立。因此
$$
\boxed{S^iB^j\in\mathcal V_{i+4j}\ \Longleftrightarrow\ i\ge4j.}
\tag{26}
$$
对 $S^iU^j$，只有 $t$ 指数减去 $j$，仍非负；同一个 (26) 完全成立。通常总次数 $i+j\le D$ 下，容纳的这些实际单项式数恰为
$$
\sum_{j=0}^{\lfloor D/5\rfloor}(D-5j+1)=D^2/10+O(D).
\tag{27}
$$
新原点抵消没有扩大此 canonical 锥或其主阶体积。

若只用角多项式补 (25) 的负阶，最小必要因子是
$$
d^{r_d}(t-1)^{r_1},\quad
r_d=(2j-\lfloor i/2\rfloor)_+,\quad
r_1=(\beta_n-i-j)_+.
\tag{28}
$$
它在原点为单位，但同 charge 还须
$r_d+r_1\le\lfloor i/2\rfloor+4$ 才不超无穷帽。这仍与 $U$ 相同；角单位不等于中央乘法单位，不据 (28) 传播中央零。

## 5. 原整个 M 的列变换和十三行

charge 四时 $q_4=a/d^2,e_5=20$，故
$$
A=\mathscr R^4q_4H_{16}/7\in\mathcal V_4,\qquad
d^2B=\mathscr R^4q_4tK_{17}/91\in\mathcal V_4,\quad
d^2U\in\mathcal V_4.
\tag{29}
$$
前一个商次数十六，后两商次数十八。未把 $J_B'=0$ 搬给 $d^2B$。

令 $\mathcal W$ 是原完整 canonical 格且含 $\mathcal V_4$，保共同载体
$$
G_0=\mathscr R^{40}
\frac{P_{134}t^{13}(t-1)^{15}h_7^{13}}{d^{17}}.
$$
在 $\mathcal W\oplus\mathcal O U$ 中改用 $\mathcal W\oplus\mathcal O B$，由
$U=B+A$ 给一个固定整列变换 $T_{\rm col}$，行列式一。$A,B,U$ 同 charge，所以它与总 Euler $\mathcal E+40$ 和完整逐 charge Gaussian 交换。对每一个原目标前缀、全部精度 $p^r$，
$$
\boxed{M_{\mathcal W,U}=M_{\mathcal W,B}T_{\rm col}.}
\tag{30}
$$
这给相同首像、全部 Smith 指数、饱和前缀及两次提升，不只是首核维数。范围是这个完整扩充格；不同两生成元格 $\mathbf Z[S,U]$、$\mathbf Z[S,B]$ 未被冒认成 (30)。

在原
$$
\Gamma=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2)
$$
中，公共 $w^{13}$ 和总 charge $n+40$ 都保持。新列首阶 $w^{i+2j}$ 不将公共十三改为十二，也不取消 $[s-13,s)$、$[2s-13,2s)$ 的两组 carry。原 $P_{134}$ 和 $U_0$ 全保。对原 primitive 三精度系统，(30) 已精确排除仅靠这次换基得到额外 ordered 收益。

## 6. 独立新格的全次数预算

真正重新选择
$$
E_D^{S,B}=\bigoplus_{i+j\le D}\mathbf Z X^iY^j,\quad
r_k(P)=[w^k]P(S,B),\quad
K_{D,k}=\ker_{\mathbf Q}(r_0,\ldots,r_{k-1})\cap E_D^{S,B}.
\tag{31}
$$
秩为 $N_D=\binom{D+2}{2}$，无自由 $w$ 列。全部范数使用这一份单项式格，不使用 (15) 的较大角环境。

### 6.1 复增长

$S,U,S(2z)$ 是固定完整 theta 截面，固定缩放及线性和给
$$
\log\max(1,|S(w)|,|B(w)|)\le C(1+|w|^{1/3}).
$$
同一 Cauchy 优化对所有 $D,k$ 的真实饱和层给
$$
\boxed{\log\|\varphi_D^k\|_\infty
\le-3k\log k+3k\log D+O(k+D).}
\tag{32}
$$
首阶二不使 $B$ 仅依赖 $w^2$，也不降低复增长阶。固定 $1/64$ 和可选 $1/1890$ 只改变固定常数。

### 6.2 普通饱和整性

原 $S,U$ 的整 Amice 测度及 $[2]_*/64$ 给 $B$ 和全部 $P(S,B)$ 的同周期有界整测度。在 (31) 的真实核上，低于 $6k$ 的全部矩零。用同一下降阶乘 $\prod_{v=0}^{6k-1}(x-v)$ 精确抵消 $(6k)!$，得到
$$
\boxed{\|\varphi_D^k\|_p\le1}
\tag{33}
$$
对全部好普通位和全部 $D,k$ 成立；不使用乘积中央零。

### 6.3 惰性包络与纯起阶收益

取 R418 的真实内盘
$$
r<r_p=p^{-p/(p^2-1)}.
$$
完整 Gaussian 收敛，$\|\Theta\|_r\le1,\|t\|_r=r^6$。由 (1)、(10)，
$$
\|S\|_r\le r^6,\qquad \|B\|_r\le r^{12}.
\tag{34}
$$
对单项式列 $\Phi_{i,j}=S^iB^j$、$\ell_{i,j}=i+2j$，
$$
[w^k]\Phi_{i,j}=0\ (k<\ell_{i,j}),\qquad
\log|[w^k]\Phi_{i,j}|_p
\le\left\lfloor\frac{6(k-\ell_{i,j})p}{p^2-1}\right\rfloor\log p
\ (k\ge\ell_{i,j}).
\tag{35}
$$
整个最大系数格再限制到 (31)，仍付
$$
\boxed{\sum_{p\equiv5(6)}\log\|\varphi_D^k\|_p
\le3k\log k+O(k+D).}
\tag{36}
$$
所有固定坏位按固定较小收敛盘计入 $O(k+D)$，没有删除未估计的无限坏集。不能把 (34) 的第二个十二换成所有列的统一十二：$S$ 仍从 $w$ 起。

即使把纯列起阶改善完整计入行列式，它仍是低阶量：
$$
\sum_{i+j\le D}(i+2j)=\frac{D(D+1)(D+2)}2,
$$
相较两来源均从 $w$ 起的情况，额外收益恰为
$$
\boxed{\sum_{i+j\le D}j=\frac{D(D+1)(D+2)}6.}
\tag{37}
$$
每个非零 $N_D$ 阶 jet 子式的每个置换项扣去同一个列阶之和。因此纯起阶在惰性素数和中的改善至多 $O(D^3\log(K+2))$，$K$ 为最大行号。另一方面，$N_D$ 个不同非负行号之和至少 $N_D(N_D-1)/2$。在 $K\asymp D^2$ 的全旗标尺度，主量是 $D^4\log D$，(37) 只有 $D^3\log D$。更大的跳跃也不将该固定列阶量变成统一的 $k\log k$ 主系数改善。

这是现有起阶包络的准确比较，不是排除未来使用原中央条件的更强估计。原 $S,U$ 也可用多项式线性剪切 $U-S$ 提升首阶；首阶变化本身不等于全饱和旗标的主项收益。

## 7. 原严格门与准确结论

同一真实秩二格的乘积公式，结合 (32)、(33)，仍给充分严格门
$$
\boxed{a_I+2b_I<3}
\tag{38}
$$
其中需要从原中央同时失败，在 (31) 的全部非零层证明
$$
\sum_{p\equiv5(6)}\log\|\varphi_D^k\|_p
\le a_Ik\log D+b_Ik\log k+O(k+D).
$$
目前 (36) 仍为 $(a_I,b_I)=(0,3)$，(37) 未满足 (38)。

所以原两中央确实传给 $S,B$，其原点链、全角格和 Gaussian 已付；但原含 $A$ 的 canonical 扩充由 (30) 保全部 ordered 成本，新两生成元格的 canonical 成员锥和主阶源体积也未增大。接续若要改善，须付该格在原中央假设下的实际全前缀估计或指定 forcing 新关系；不能继续仅按倍点列数、首阶或清极乘子计算收益。

## 8. 固定公开运行与依赖

Producer：
[check-same-charge-doubled-s-and-u-source.py](../scripts/check-same-charge-doubled-s-and-u-source.py)。
~~~sh
python3 topics/rank2-sha-infinitely-many-p/scripts/check-same-charge-doubled-s-and-u-source.py
~~~
无参数，程序仅用 Python 标准库。它从 (2)–(9) 重建完整多项式，核倍点因子、固定角阶、$K_{17}$ 与 $ad$ 互素、首项1890及实际次数十七。没有目标素数扫描。

- Source commit：76ea69cd6ecb82aaecfd3a164187e955595bfe23。
- GitHub Actions run：43749289064；job：132919420622。
- Script SHA-256：f6f64cea6578c84f82af93bc7bb161b4b73563dcd7c0ce94984eadf3af293fc8。
- Stdout：1482 bytes；SHA-256：82bbc651d116f9081f1a2a3ae675349aa81a87102718d4c5c56594ae1fc17d37。
- Exit code：0。输出不入仓库，只保脚本、参数、run 和 hash。

全部无界 floor、前缀、所有精度列变换及全局预算由正文证明；固定多项式结果不代目标素数非消失。

依赖：

- [R314](R314-jzero-actual-doubling-return-and-full-q2-transport.md)：原倍点全 Mellin/Newton 转置、三块尺度 carry。
- [R365](R365-whole-original-conductor-carrier-and-total-charge-connection.md)：完整 canonical floor、$P_{134}$、总 charge 与十三行。
- [R418](R418-jzero-two-source-growth-and-full-degree-slope-budget.md)：真正饱和旗标、普通阶乘抵消、惰性半径及严格预算。
- [R466](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)、[R468](R468-third-original-central-row-three-axis-hensel-and-six-carry-interface.md)：原 $U_{136}$、完整第三中央与三权。
- [R473](R473-three-source-function-field-normalization-and-integral-conductor.md)：固定 $H_{18}$ 和来源域范围；未借规范化给乘积中央零。
