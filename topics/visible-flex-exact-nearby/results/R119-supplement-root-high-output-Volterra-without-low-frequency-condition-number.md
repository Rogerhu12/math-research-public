# R119 续篇：实际根的全输入高输出 Volterra 界，不再乘低频条件数

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇在第51束的同一个实际 canonical 根中，改进两次 Volterra 余项。输入不截断，包含 mean、两条 wave 行和两个 Fourier 锥。对真实根斜率 $b>1$，置

$$
L_b=2^{4200}b,\qquad P_b=\mathbf1_{\{|m|\ge L_b\}}.
\tag{V.1}
$$

令 $U(\xi,\eta)$ 是第51束完整 Airy interaction 演化，$K$ 是其准确 generator，$0\le\eta\le\xi\le H=1/64$。则对 $|s|\le1$，

$$
\boxed{\quad
\|P_b U(\xi,\eta):H^s\to H^s\|<2,
\quad
\left\|P_b\left[U(\xi,\eta)-I-
               \int_\eta^\xi K(q)\,dq\right]:
       H^s\to H^{s+4/3}\right\|
       <2^{4096}b^{4/3}.
\quad}
\tag{V.2}
$$

完整逆向演化满足同样的结论。这里的第二式是全 Hilbert 算子界：第6节支付了 dyadic 频带的行和列，不能将单个输出 shell 的 supremum 当作该结论。

这只改进**真实根的二次 Volterra 部分**。一次积分的首符号拆分、真实 root graph、严格区、完整正型 Cayley 及全网络的 source wiring 必须分别消费；本篇不据此宣称旧 $T_j$ 已被 $\delta_j^{-9}$ 替换。原 Γ* 两列和 ordinary/weak 源没有设为零。

## 1. 同一个对象与真正可用的旧界

所有对象与 [实际完整余项和高网络](R119-supplement-actual-nonradial-full-remainder-and-high-network.md) §4 完全相同：

$$
u_{\xi\xi}-{\xi\over b^2}u_{\phi\phi}+V(\xi,\phi)u=0,
\qquad 0\le\xi\le H,
\tag{V.3}
$$

物理角周期为 $\pi/2$，$m\in4\mathbb Z$。沿其已付角条带，$|V|<17$；所需 $\xi$ 范围和复邻域仍是原真实根图的域。完整自由 Airy 矩阵记为 $F_m$，mean 使用原 $c(1\pm i\xi/\pi)$ 两列，不代入 $m^{-1}$。准确有

$$
K_{mn}(\xi)=F_m(\xi)^{-1}
 \begin{pmatrix}0&0\\-V_{m-n}(\xi)&0\end{pmatrix}F_n(\xi),
\qquad U_\xi=KU.
\tag{V.4}
$$

原 (H.15)–(H.16) 已经给全输入、全输出的

$$
\|K:H^r\to H^{r+2/3}\|<2^{128}b^{2/3},\qquad
\|U(\xi,\eta)^{\pm1}:H^0\to H^0\|
       <G_b:=2^{2217}b^{2/3}.
\tag{V.5}
$$

同一旧界适用于任意两个 collar 截面，并非仅适用于一个端点。下面先使用第二个旧界控制截断 commutator，随后才改进高输出；未循环假定高输出已小。

以 $\langle m\rangle=(1+m^2)^{1/2}$ 表示原 Sobolev 权。由实际 Airy height 两行界和准确常数 Wronskian，(V.4) 的每个 $2\times2$ block 有

$$
\|K_{mn}\|\le
2^{16} b^{2/3}\langle m\rangle^{-1/3}
                   \langle n\rangle^{-1/3}|V_{m-n}|.
\tag{V.6}
$$

两个 height 因子分别来自 $F_m^{-1}e_2$ 和 $e_1^TF_n$。因此 (V.6) 包括 mean、跨锥和全部 angular lag；它不需要把输入限制在某一高锥。

下文最多使用二十阶 lag moment。宽 $1/128$ 给

$$
 |V_l|\le17e^{-|l|/128},\qquad
 \sum_{l\in4\mathbb Z}(1+|l|)^{14}|V_l|<2^{180},\qquad
 \sum_{l\in4\mathbb Z}(1+|l|)^{20}|V_l|<2^{260}.
\tag{V.7}
$$

例如将指数分成两个 $e^{-|l|/256}$，用
$x^r e^{-x/256}\le r!256^r$、
$(1+x)^r\le2^{r-1}(1+x^r)$ 和
$\sum_{l\in4\mathbb Z}e^{-|l|/256}<513$。
这条宽放上界只用整数与初等指数比较；之后没有再使用一个未付的径向高导数。

## 2. 两个完整 kernel 门

以下 $M\ge64$。取实平滑乘子 $\chi(D/M)$，满足

$$
\chi=0\ (|m|\le M/2),\quad
\chi=1\ (|m|\ge M),\quad
0\le\chi\le1,\quad
\operatorname{Lip}(\chi(D/M))\le8/M,
\tag{V.8}
$$

并置 $Q=\mathbf1_{\{|m|\ge M/4\}}$。于是 $Q\chi=\chi$。Schur 对 (V.6)–(V.7) 给

$$
\int_\eta^\xi\|QKQ\|\,dq
 <A_M:=2^{300}(b/M)^{2/3},
\tag{V.9}
$$

$$
\int_\eta^\xi\|Q[\chi,K]\|\,dq
 <C_M:=2^{300}b^{2/3}M^{-5/3}.
\tag{V.10}
$$

完整 lag 分法如下。

* 若 $|m-n|\le\max(|m|,|n|)/4$ 且 $\chi_m\ne\chi_n$，两频率可比且至少一个在 transition 带中，故两者都大于 $M/4$。两个 height 因子给 $2^2M^{-2/3}$，而 $|\chi_m-\chi_n|\le8|m-n|/M$ 再给一阶。
* 在其余项中，只要 commutator 非零，就有 $|m-n|\ge M/16$。保留 (V.6) 的完整两因子，再用 (V.7) 的 lag moment。这样 mean 和相反 Fourier 符号也参加同一次 Schur 求和。

同样，如果两个 sharp 频率集合相隔至少 $M/16$，并且一个位于 $|m|\ge M/2$、另一个位于 $|m|\le M/4$，则

$$
\int_\eta^\xi\|P_1 K P_2\|\,dq
 <2^{320}b^{2/3}M^{-12}.
\tag{V.11}
$$

本式双向成立。直接付 $$M/16$^{-12}$ 后只需十四阶 lag moment；$16+180+48+4<320$ 包含 $16^{12}$、两行、两个 Fourier 符号及 Schur 行列两侧。过宽的 $2^{300},2^{320}$ 不含额外 $b$ 幂。

后面将把 (V.8) 的阈值整体缩小至 $M/4$ 或 $M/16$。同一个证明在这些尺度使用；为了统一记号，可将 (V.9)–(V.11) 的 $2^{300},2^{320}$ 放宽为 $2^{320},2^{400}$。

## 3. 平滑截断直接作用于全部输入

先不用输入投影。令 $W=\chi U$。准确微分为

$$
 W'=QKQW+Q[\chi,K]U,\qquad W(\eta)=\chi.
\tag{V.12}
$$

等号成立是因为 $Q\chi=\chi$，并非把 $K$ 与高投影交换。由全空间旧界 (V.5)，

$$
\sup\|W\|\le e^{A_M}(1+C_MG_b).
\tag{V.13}
$$

若 $M\ge2^{4096}b$，则

$$
A_M<2^{-2400},\qquad C_MG_b<2^{-4000}.
\tag{V.14}
$$

例如未放宽的二进制指数分别为

$$
300-\tfrac23\,4096<-2400,
\quad 300+2217-\tfrac53\,4096<-4000;
$$

第二式还留下 $b^{-1/3}\le1$。因此

$$
\boxed{\quad
\|\mathbf1_{\{|m|\ge M\}}U(\xi,\eta):H^0\to H^0\|<2
\quad(M\ge2^{4096}b).
\quad}
\tag{V.15}
$$

输入可以是 mean 或任意低频历史。这里没有假定低到高输出为零。

## 4. 真实二次 Volterra 的输出行

记

$$
R=U-I-\int_\eta^\xi K(q)\,dq
 =\int_{\eta<q_2<q_1<\xi}
      K(q_1)K(q_2)U(q_2,\eta)\,dq_2dq_1.
\tag{V.16}
$$

令 $M\ge2^{4200}b$。在第一个 $K$ 后插入频率阈值 $M/2$，在第二个 $K$ 后插入 $M/4$。两次相邻项由 (V.5)、(V.15) 给

$$
2^{330}b^{4/3}M^{-4/3}.
$$

若任一插入落在远 lag 部分，使用 (V.11)，其余 $K$ 使用全空间 (V.5)，完整 $U$ 使用旧 $G_b$。两个远项分别小于

$$
2^{2700}b^2M^{-38/3},\qquad
2^{2700}b^2M^{-12}.
$$

这些都严格小于 $2^{2700}b^{4/3}M^{-4/3}$，因为 $M\ge b>1$。三项合计可以统一记为

$$
\boxed{\quad
\|P_{\{|m|\ge M\}}R:H^0\to H^0\|
 <2^{2800}b^{4/3}M^{-4/3}.
\quad}
\tag{V.17}
$$

这里只得到输出行。下一节专门支付强 Sobolev 结论所需的远频带衰减。

## 5. 两个 nested buffers 支付远频带

设初始输入在 $|n|\le M/16$。取第一 cutoff 如 (V.8)，第二 cutoff 在 $M/8$ 以下为0、在 $M/4$ 以上为1。记为 $\chi_1,\chi_2$，其对应 $W_r=\chi_r U P_{\{|n|\le M/16\}}$ 都具有零初值。

第一 commutator 准确拆成

$$
 Q_1[\chi_1,K]U
 =Q_1[\chi_1,K]W_2
       +Q_1[\chi_1,K](I-\chi_2)U.
\tag{V.18}
$$

第二项所有非零 kernel 都有 lag 至少 $M/16$：若 $\chi_2(n)\ne1$，则 $|n|<M/4$，而 $\chi_1(m)-\chi_1(n)\ne0$ 强迫 $|m|>M/2$。因此它使用 (V.11)，而不是再粗用一次无局部性的 commutator 范数。

先对 $W_2$ 使用 (V.12) 的零初值版本，再对 $W_1$ 使用 (V.18)，得

$$
\|W_2\|<2^{2540}b^{4/3}M^{-5/3},
$$

$$
\|W_1\|<2^{3000}
       [b^2M^{-10/3}+b^{4/3}M^{-12}].
\tag{V.19}
$$

这两个常数分别包含旧 $2^{2217}$、每次缩放 cutoff 的 $2^{320}$ 和小于2的 Gronwall 因子。扣除同样是远 lag 的 $\int K$，并用 $M\ge b$，得到

$$
\boxed{\quad
\|P_{\{|m|\ge M\}}R P_{\{|n|\le M/16\}}\|
 <2^{3010}b^{4/3}M^{-8/3}.
\quad}
\tag{V.20}
$$

不能只用 (V.17) 替代这条远带门。

真实实背景下，完整 wave Green 矩阵是常数 $\mathsf J=\operatorname{diag}(I,-I)$，且

$$
K^*\mathsf J+\mathsf JK=0,
\quad U(\xi,\eta)^*=\mathsf J U(\eta,\xi)\mathsf J.
\tag{V.21}
$$

逆向的一阶积分取反。因此 $R^*=\mathsf J R_{\rm back}\mathsf J$。对相反方向重复以上证明，即给 (V.20) 的输入/输出反向版本。不存在未付的 adjoint 演化范数。

## 6. 真正的频带 Schur，而非 shell supremum

将 $m\in4\mathbb Z$ 按 dyadic 的 $\langle m\rangle$ 分组；包含 mean 的第一组权为1。记输出尺度 $M$、输入尺度 $N$。改变 sharp 端点及 $|m|$ 与 $\langle m\rangle$ 只需固定的2倍尺度和8倍范数；(V.1) 的余量包含这些改动。

若 $M/32\le N\le32M$，(V.17) 给加权 block

$$
 M^{s+4/3}\|R_{MN}\|N^{-s}
 <2^{2820}b^{4/3},\qquad |s|\le1.
\tag{V.22}
$$

每行每列至多13个这样的 block。若 $N<M/32$，(V.20) 给

$$
 M^{s+4/3}\|R_{MN}\|N^{-s}
 \le2^{3030}b^{4/3}M^{-1/3}N^{-1}.
\tag{V.23}
$$

这是用最坏的 $(M/N)^{|s|}\le M/N$ 得到的共同上界。dyadic 的

$$
\sum_{N\le M/32}N^{-1}<2,\qquad
\sum_{M\ge32N}M^{-1/3}<8N^{-1/3}
\tag{V.24}
$$

使它的每行、每列和均小于 $2^{3040}b^{4/3}$。若 $N>32M$，反向 (V.20) 给

$$
 M^{s+4/3}\|R_{MN}\|N^{-s}
 \le2^{3030}b^{4/3}M^{1/3}N^{-5/3}.
\tag{V.25}
$$

相应两条 dyadic 几何级数的和小于8，仍有同一个 $2^{3040}b^{4/3}$ 门。

block Schur 测试由这些行、列和直接给

$$
\|P_bR:H^s\to H^{s+4/3}\|<2^{3050}b^{4/3}
 <2^{4096}b^{4/3}.
\tag{V.26}
$$

本证明先在有限 Fourier 数据上作准确矩阵运算，最后按此一致算子界延拓；没有删去低输入的无限输出，也没有使用径向有限支持在 $\ell^\infty$ 中稠密这一错误断言。

最后由 $U=I+\int K+R$，(V.5)、(V.26) 和 (V.1)，

$$
\|P_bU:H^s\to H^s\|
 \le1+2^{128}(b/L_b)^{2/3}
          +2^{4096}(b/L_b)^{4/3}<2.
\tag{V.27}
$$

这完成 (V.2) 的全部量词。逆向、双号、mean 输入的证明已经包含在前面。

## 7. 源、参数和这条新界的权限

若原完整 interaction 方程有源 $Y'=KY+s$，同一 (V.15)、(V.27) 对任意两个截面成立，因此

$$
 \left\|P_b\int_\eta^\xi U(\xi,q)s(q)\,dq\right\|_{H^s}
 <2\int_\eta^\xi\|s(q)\|_{H^s}\,dq,\qquad |s|\le1.
\tag{V.28}
$$

这里 $s=F^{-1}s_{\rm canonical}$ 必须仍是原完整两行源。ordinary 项保留实际材料密度及 Jacobian；weak 项先换为 total flux，保两分量和真实端点 $F^t$ 荷。本篇不从一个体源 $L^1$ 范数推导 bare-flux 端点迹，也不对 weak $F^t$ 求径向导数。

在第55束同一个 joint $\Gamma^*(\mathbf a,\Omega)$ 上，(V.3)–(V.7) 原有界统一成立，因此本篇作用于全部真实背景。若把 $D\Gamma^*$ 两列或其它参数响应放入有源方程，它们是 (V.28) 的实际源列，不会被本高频投影自动消去。原物理源到 canonical $s$ 的换算界仍按已证合同消费。

与旧 (H.16) 的区别是：二次 Volterra 的 high 部分现在只收 $b^{4/3}$，不再收 $b^{4/3}\times b^{2/3}=b^2$。这没有取消一次首符号、graph Jacobian、真实正片 cross 或外部返回的任何费用。要得到一个新的全网络 cutoff，仍须把这些其余因子放进相同原单位后完成实际比较。

## 8. 可复算预算与执行约定

[预算源码](../scripts/fourfold_root_high_output_volterra_20261114.py) 检查本篇新增的 lag-moment、cutoff 指数、远带幂、dyadic 行列求和及原 source 权限，并绑定实际依赖文件的 SHA256。它不以数值样本证明 Fourier 全范围或 ODE 恒等式。

依用户要求，新执行只放在本公开仓库 GitHub Actions。命令为

```bash
python3 topics/visible-flex-exact-nearby/scripts/fourfold_root_high_output_volterra_20261114.py --manifest topics/visible-flex-exact-nearby/notes/2026-11-14-R119-root-high-output-volterra-inputs.json --out topics/visible-flex-exact-nearby/notes/2026-11-14-R119-root-high-output-volterra-budget.json
```

实际执行结果以该 native 为准；未运行的门不得填写成通过。本篇没有恢复或重跑旧大规模科学源。
