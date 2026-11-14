# R439 — 原残余伴随的完整两态 core 与真实隐藏同深块比较

日期：2026-11-14。**状态：已证明。** 在 R431 的固定 ray 上再作一次
固定模七细分，R437 的同一个残余来源 $\mathcal L$ 的伴随方向可以
完整支付。整个 degree7280 空间满足
$$
K_{7280}^2=\frac12\sum_{t\in E[2]}T_t^{(7280)}-I,\qquad
K_{7280}^4=I.
$$
绝对平方由 R370 已证明的 degree5 原来源定标，不假定一个未付的
一般 theta 相位公式。

实际 $\mathcal L$ 在伴随二挠群下固定，因此只需两条固定来源：
$$
\mathcal L_0=\mathcal L,\qquad
\mathcal L_1=\frac18\sum_{t\in E[4]}T_{t,Q}^{(7280)}\mathcal L.
$$
它们的完整 $W$ core 均为 $-\lambda$，完整伴随 core 为
$\eta_{5,p}\lambda$ 乘两态交换，其中 R370 的真实符号
$\eta_{5,p}\in\{\pm1\}$ 不需猜定。尤其偶数 $n$ 时，残余两个输出
同时深的完整测度准确为 $\lambda^{2n}$ 乘共同缩放。
这也使 R437 的原隐藏同深块与整个残余双深输出域之间得到一个
明确的完整测度比例；没有把这两个不同事件直接相认。

## 1. 同一个残余来源，两个输出都保留

沿用 R430、R431、R435、R437 的原曲线 $b=17$、sigma、周期，
以及
$$
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\lambda=-\bar\pi_0^{-1},\quad
\kappa=p/\bar\pi_0^2,\quad p>19.
\tag{1}
$$
原小核为
$$
\mathcal K(y,v)=G_{16}(y)\sigma(y-v)\sigma(y+v)\mathcal R(y,v),
\qquad G_{16}(y)=\frac{\sigma(2y)\sigma(2\delta y)}{4\delta}.
$$
作 R431 的同一坐标 $y=w+9q,\ v=w-17q$，得到
$$
\mathcal K(w+9q,w-17q)=\sigma(26q)\mathcal L(w,q),
\tag{2}
$$
其中是真正全纯整来源
$$
\boxed{
\mathcal L(w,q)=\frac1{4\delta}
 \sigma(2w+18q)\sigma(2\delta w+18\delta q)
 \sigma(2w-8q)\mathcal R(w+9q,w-17q).
}
\tag{3}
$$
每个因子与 R437 相同，没有只保相同边际而重新构造联合。

由 $\mathcal R\in\mathcal S_{16}\boxtimes\mathcal S_{16}$，完整
$W,Q$ degree 和交叉项为
$$
N_W=4+12+4+16+16=52,
$$
$$
N_Q=324+972+64+16(81+289)=7280,
$$
$$
36+108-16+16(9-17)=0.
\tag{4}
$$
三个 sigma 的两个方向系数全为偶 CM 整数，原奇半特征在两个
方向都成为平凡；$\mathcal R$ 的 degree 为偶。因此
$$
\boxed{\mathcal L\in
 \mathcal S_{52}\boxtimes\mathcal S_{7280}}
\tag{5}
$$
是完整无 twist 的 theta 张量格。原 Amice 乘积整，而标准
正式群首阶基的系数消元支付 (5) 的整张量性。

(2) 的 $\sigma(26q)$ 只含伴随变量。R431 的 $W$ division trace
可与该因子交换；在完整形式幂级数整环中约去这个非零因子，
R437 已严格得到
$$
\boxed{(K_{52}\otimes I)\mathcal L=-\mathcal L,\qquad
\nu_{\mathcal L}|_{W\in p}
=-\lambda[\kappa,1]_*\nu_{\mathcal L}.}
\tag{6}
$$
这里不要求 $\sigma(26q)$ 是 Amice 单位，也不将 $Q$ trace
错误地穿过同轴 sigma 因子。

## 2. 一次固定的模七细分

R431 的原 ray 是
$$
\pi_0\equiv13657087+21407490\omega\pmod{36279360}.
$$
在其上加 $\pi_0\equiv2\pmod7$，准确 CRT 代表为
$$
\boxed{\pi_0\equiv158774527+130245570\omega
                    \pmod{253955520}.}
\tag{7}
$$
旧模数不含七，新增类为单位，且新条件给 $p=N\pi_0\equiv4\pmod7$。
原 primary、两曲线角色和所有旧单位结论均保留。
这是一条固定非空 ray 类；原有限类域论的素理想定理仍给无穷多个
普通有理素数。没有随 $p$ 另选参数。

$7280=16\cdot5\cdot7\cdot13$。旧条件给模五、十三的 ratio 为一，
新条件给模七为一；模三十二仍是 R435 的原 ratio。因此
$$
\boxed{
g=\pi_0/\bar\pi_0\equiv10011+10920\omega\pmod{14560},
}
$$
$$
\boxed{
g^2\equiv3641+7280\omega,\qquad
g^4\equiv7281\pmod{14560}.}
\tag{8}
$$
例如第一式模三十二为 $27+8\omega$，模 $455$ 为一。
以下平方证明保留完整模 $2N$，不把 (8) 只读成模 $N$ 的实整数。

## 3. 整个 degree7280 的真实平方形状

暂记 $N=7280$，使用原规范
$$
T_t^{(N)}F(z)=e^{-N\eta_t(z+t/2)}F(z+t),\qquad
K_N=\frac{\bar\pi_{17}}p\mathscr M_{\pi_{17}},
$$
$$
\nu_F|_p=\lambda[\kappa]_*\nu_{K_NF},
\qquad \pi_{17}=-\pi_0.
\tag{9}
$$
在整个 $N$ 维 Schrödinger 基中取
$Xe_j=\zeta_N^je_j,\ Ze_j=e_{j+1}$。
由 (8)，$g^2$ 对两个格基的像为
$$
3641+N\omega,\qquad -N-3639\omega .
$$
两条对称 Heisenberg lift 的交叉指数模 $2N$ 都等于 $N$。
所以真实平方交织准确是
$$
\boxed{K_N^2X(K_N^2)^{-1}=-X^{3641},\qquad
K_N^2Z(K_N^2)^{-1}=-Z^{3641}.}
\tag{10}
$$
两个负号都属于完整中心。

因 $N/4=1820$ 为偶，对 $t=(s+r\omega)/2$，
$$
T_t^{(N)}e_j=(-1)^{sj}e_{j+Nr/2}.
$$
定义固定整算子
$$
B_N=\frac12\sum_{t\in E[2]}T_t^{(N)}-I.
$$
直接求和给
$$
\boxed{B_Ne_j=(-1)^j e_{3641j+3640},\qquad B_N^2=I.}
\tag{11}
$$
它实现与 (10) 相同的两个交织。原完整 Heisenberg 表示不可约，
故 $K_N^2$ 与 $B_N$ 只差一个标量。
下节用一个已经支付真实 core 的原非零锚固定这个标量。

## 4. R370 的实际 degree5 锚付清绝对平方

R370 的同一原来源是
$$
F_{12}(z)=\sigma(z)\sigma(2z)=-2y(z)\sigma(z)^5
\in\mathcal S_5,\qquad F_{12}=2z^2+\cdots.
\tag{12}
$$
R370 §§2–5 已完整支付奇 degree 的半特征、原 two-input
theta 联合、实际 trace 和全周期运输。其真实符号
$\eta=\eta_{5,p}\in\{\pm1\}$ 满足
$$
\nu_{F_{12}}|_p
=\frac{\varepsilon^5\eta u_5^{-1}}{\bar\pi_{17}}
                 [\kappa]_*\nu_{F_{12}},
\quad
u_5\equiv\pi_0/\bar\pi_0\pmod5 .
\tag{13}
$$
当前 ray 有 $\varepsilon=\pi_0/\pi_{17}=-1$、
$\pi_0\equiv2\pmod5$，故 $u_5=1$，于是
$$
\boxed{\nu_{F_{12}}|_p
=-\eta\lambda[\kappa]_*\nu_{F_{12}}.}
\tag{14}
$$
这里使用的是 R370 的已证平方约束，不从一维投影或有限 CM7
样本猜定 $\eta$ 的值。

置
$$
\gamma_7=3+\omega,\qquad\gamma_{13}=4+\omega,\qquad
\beta=\gamma_7\gamma_{13},\qquad \alpha=4\beta.
$$
$N\beta=91,\ N\alpha=1456$，所以
$$
A_*(z)=F_{12}(\alpha z)\in\mathcal S_{5N\alpha}
=\mathcal S_{7280}.
\tag{15}
$$
$\alpha$ 是当前普通处的单位，故 (14) 与该实际尺度推前交换：
$$
K_{7280}A_*=-\eta A_*,\qquad K_{7280}^2A_*=A_*.
\tag{16}
$$
对任意 $t\in E[2]$，$\alpha t\in2\Lambda$ 且
$2\alpha t\in4\Lambda$。两个原 odd sigma 的半特征均为正，
规范指数与拉回相消。因此
$$
T_t^{(7280)}A_*=A_*\quad(t\in E[2]),\qquad B_NA_*=A_*.
\tag{17}
$$
(16)–(17) 固定第3节的唯一标量为一，得到整个空间的绝对身份
$$
\boxed{
K_{7280}^2=B_N=\frac12\sum_{E[2]}T_t^{(7280)}-I,
\qquad K_{7280}^4=I.}
\tag{18}
$$
不需要知道 $\eta$。没有将项目交织自动提升为 (18)。

## 5. 实际残余在全部伴随二挠平移下固定

在 (3) 中对 $q$ 平移任意 $t\in E[2]$。

前两个 sigma 分别平移 $18t,18\delta t$；
非零 $t$ 时两者各给负半特征，因为 $\delta\equiv1\pmod2$，
两个负号相消。第三个 sigma 平移 $-8t\in4\Lambda$，给正号。
$\mathcal R$ 的两输入平移为 $(9t,-17t)$，在完整 degree16 lift
中可准确还原为 $(t,t)$：其差是原格周期，且 degree16 的相关
中心指数均为偶数。R435 已付
$(T_t^{(16)}\otimes T_t^{(16)})\mathcal R=\mathcal R$。

这些逐因子 lift 的所有 $w$ 指数由 (4) 的完整交叉和相消，
$q$ 指数恰合成 degree7280 的规范指数，故得到整个联合式
$$
\boxed{(I\otimes T_t^{(7280)})\mathcal L=\mathcal L
\qquad(t\in E[2]).}
\tag{19}
$$
它不只是 $q=0$ 边际上的关系。由 (18)，
$$
\boxed{(I\otimes K_{7280}^2)\mathcal L=\mathcal L.}
\tag{20}
$$

## 6. 降到 degree1820，付出两态第一步的固定公式

完整二挠固定空间是 $[2]^*\mathcal S_{1820}$。
具体地，$[2]^*$ 的像被四个规范二挠 lift 固定；它的维数为
$1820=7280/4$，等于 Schrödinger 表示中固定空间的维数。
因此 (19) 使唯一的整来源 $\overline{\mathcal L}$ 满足
$$
\boxed{\mathcal L(w,q)=\overline{\mathcal L}(w,2q),\qquad
\overline{\mathcal L}\in\mathcal S_{52}\boxtimes\mathcal S_{1820}.}
\tag{21}
$$
整性也直接由 Amice 变量中单位尺度 $1/2$ 的推前给出。

记 $n_*=1820$。从 (8) 约化到完整模 $2n_*=3640$，得到
$$
g\equiv2731\pmod{3640}.
$$
其在标准基中的交织由 $D e_j=e_{911j}$ 实现，因为
$2731\equiv911\pmod{1820}$ 且 $911^2\equiv1\pmod{1820}$。
$n_*/4=455$ 为奇，所以完整二挠公式是
$$
T_{(s+r\omega)/2}^{(1820)}e_j
=(-1)^{s(r+j)}e_{j+910r}.
$$
因此在整个 degree1820 空间上
$$
D=\frac12\sum_{t\in E[2]}T_t^{(1820)},\qquad D^2=I.
\tag{22}
$$

用真实非零锚 $F_{12}(2\beta z)$ 定标。
其 degree 是 $5N(2\beta)=1820$；非零二挠平移在第一个
sigma 因子中给负号、第二个给正号，所以 $D$ 在锚上为 $-1$。
(14) 则使真实 $K_{1820}$ 在同一锚上为 $-\eta$。
完整不可约性于是给
$$
\boxed{K_{1820}=\eta\,D
=\frac{\eta}{2}\sum_{t\in E[2]}T_t^{(1820)}.}
\tag{23}
$$
这是真正的绝对第一步公式；$\eta$ 是原算子固定的实际符号。

[2] 拉回与普通 core 交换，且将 $T_t^{(1820)}$ 拉回为
$T_{t/2}^{(7280)}$。在 (19) 的固定空间中，每个半点代表的选择
无关，因为相差二挠 lift；完整 E[4] 和将每个代表数四次。
定义两个不随 $p$ 改变的实际来源
$$
\boxed{
\mathcal L_0=\mathcal L,\qquad
\mathcal L_1=\mathcal A_Q\mathcal L,\qquad
\mathcal A_Q=\frac18\sum_{t\in E[4]}T_{t,Q}^{(7280)}.
}
\tag{24}
$$
由 (21)–(23)，$\mathcal A_Q^2\mathcal L=\mathcal L$，
且 $\mathcal L_1$ 也满足 (19)。分母只有二的幂，所有 prime-to-$p$
theta lift 保整格。真实 (23) 同时保证该完整和回到原系数域。

作为原 $y,v$ 的实际因式，(24) 还可写成
$$
\boxed{
\mathcal L_1
=\sigma(y+v)\,\frac18\sum_{t\in E[4]}
 (T_t^{(16)}G_{16})(y)\,
 ((T_t^{(16)}\otimes T_{-t}^{(16)})\mathcal R)(y,v),
}
\tag{25}
$$
仍按 $y=w+9q,\ v=w-17q$ 读取。
这里 $9t$ 与 $t$、$-17t$ 与 $-t$ 分别相差偶格点；
第三 sigma 的平移 $-8t$ 也在偶格中，故完整 lift 没有额外符号。
(25) 显示了新状态的全部有限来源，没有只命名一个未知同边际态。

## 7. 完整 W/Q 两态核心和所有输出深度

$W$ 算子与全部 $Q$ 平移交换，所以 (6)、(24) 对两态都给
$K_W\mathcal L_i=-\mathcal L_i$。完整测度式是
$$
\boxed{
\begin{aligned}
\nu_{\mathcal L_i}|_{W\in p}
 &=-\lambda[\kappa,1]_*\nu_{\mathcal L_i},\\
\nu_{\mathcal L_i}|_{Q\in p}
 &=\eta\lambda[1,\kappa]_*\nu_{\mathcal L_{1-i}},
\qquad i=0,1.
\end{aligned}}
\tag{26}
$$
每条都保另外一个完整输出的任意连续测试。
这只是至多两态；不必为使用它另外证明两个来源线性无关。

正交两轴可交换，因此所有深度准确满足
$$
\boxed{
\nu_{\mathcal L_i}|_{\{W\in p^a,\ Q\in p^b\}}
=(-\lambda)^a(\eta\lambda)^b
 [\kappa^a,\kappa^b]_*\nu_{\mathcal L_{\,i+b\bmod2}}.
}
\tag{27}
$$
特别任意偶数 $n\ge0$，
$$
\boxed{
\nu_{\mathcal L}|_{\{W,Q\in p^n\}}
=\lambda^{2n}[\kappa^n,\kappa^n]_*\nu_{\mathcal L}.}
\tag{28}
$$
此处两个负号和 $\eta^n$ 全部为一，原尺度仍完整保留。

## 8. 物理残余坐标和独立 sigma 的准确运输

令 $(Z,H)$ 为剥去 R437 那一个 sigma 后的两个原物理输出：
$$
W=Z+H,\qquad Q=9Z-17H,\qquad
\binom{Z}{H}=\frac1{26}
 \begin{pmatrix}17&1\\9&-1\end{pmatrix}\binom{W}{Q}.
\tag{29}
$$
矩阵在当前普通处整可逆，所以 (28) 也等价于
$$
\boxed{
\nu_{\mathcal L}^{\,\mathrm{phys}}|_{\{Z,H\in p^n\}}
=\lambda^{2n}[\kappa^n,\kappa^n]_*
                         \nu_{\mathcal L}^{\,\mathrm{phys}}
\quad(n\ \text{偶数}).}
\tag{30}
$$
原 $\mathcal K$ 联合准确由一个独立 sigma 输入 $c$ 恢复：
$$
Y=Z+c,\qquad X=H-c,\qquad
W=Z+H,\qquad Q_{\mathrm{tot}}=Q+26c .
\tag{31}
$$
因此 (27) 可与 $c$ 的任意连续测试和深度条件一起使用。

但是伴随限制是 $Q_{\mathrm{tot}}-26c\in p^b$。
它不是 R431 对整个 $Q_{\mathrm{tot}}$ 的限制。
例如残余伴随一层缩放在原 $Y,X,c$ 上准确为
$$
Y\longmapsto Y+\frac{\kappa-1}{26}(Q_{\mathrm{tot}}-26c),
\quad
X\longmapsto X-\frac{\kappa-1}{26}(Q_{\mathrm{tot}}-26c),
\quad c\longmapsto c .
\tag{32}
$$
这个移动中心不能删除。

对任意连续 $f(Y,X,c)$，(30) 给完整可用的式子
$$
\boxed{
\begin{aligned}
&\int_{\substack{Z,H\in p^n\\c\in\mathbf Z_p^\times}}
 f(Z+c,H-c,c)\,d\nu_{\mathcal L}^{\mathrm{phys}}d\nu_\sigma(c)\\
&\qquad=\lambda^{2n}
 \int_{c\in\mathbf Z_p^\times}
 f(\kappa^n Z+c,\kappa^n H-c,c)\,
                  d\nu_{\mathcal L}^{\mathrm{phys}}d\nu_\sigma(c)
\end{aligned}}
\tag{33}
$$
对每个正偶数 $n$ 成立。$Y,X$ 在此均为单位，$W$ 为深输出。
它允许 R441 使用原 $Y$ 中央与完整 $X^6$ 测试，但自身不把这份
真实隐藏限制从 R430 的完整条件中央中去掉。

## 9. 原隐藏同深输入与完整双输出深域的精确比例

使用 R432/R437 的平衡表示。令 $m\ge0$，
$M=2m+1$、$q_m=2\delta^{-m}$，
共有 $M$ 对原 Theta sigma 输入，保留它们的全部二次权和尺度。
设带尺度的 Theta 相加输出为 $\tau$。残余物理输出是
$$
Z=r_0+\tau+q_m(a+b_0)+e,\qquad H=s_0+e.
\tag{34}
$$
底层为同一个 $\nu_{\mathcal R}(r_0,s_0)$、三个独立 sigma 输入
$a,b_0,e$ 及 $2M$ 个带原二次权的 sigma 输入，
全局常数仍为 $\delta^{2m}/4$。

令 $\ell_{m;n,n}$ 为它们**每个**原输入都取深度 $n$ 的完整
$(Z,H)$ 推前，且 $n\in4\mathbf Z_{\ge0}$。
R435 的两个 $\mathcal R$ 输出各给 $\lambda^n$；
三个 sigma 各给 $\lambda_\sigma^n$；
$M$ 对原 sigma 给 $\lambda_\sigma^{2Mn}$，二次权另给
$\kappa^{2Mn}$。当前 $\lambda_\sigma=-\lambda$，$n$ 为四的倍数，
故准确有
$$
\ell_{m;n,n}
=\lambda^{(5+2M)n}\kappa^{2Mn}
 [\kappa^n,\kappa^n]_*\nu_{\mathcal L}^{\mathrm{phys}}.
\tag{35}
$$
与 (30) 比较，得到真正的完整测度比例
$$
\boxed{
\ell_{m;n,n}
=\lambda^{(3+2M)n}\kappa^{2Mn}
       \bigl(\nu_{\mathcal L}^{\mathrm{phys}}
                        |_{\{Z,H\in p^n\}}\bigr).
}
\tag{36}
$$
它允许张量一个相同的独立 $c$ 测试、使用任意输出测试后再积分，
不是只在原点质量或一条中央行上的等式。

(36) 的比例有准确赋值 $2Mn$，一般不是单位。
原隐藏同深事件严格包含在完整双输出深域中；两者的补集并未消失。
如果把原底层测度按这一事件及其补集分拆，再只推到显示的
$(Z,H)$，该完整补集推前准确是
$$
\boxed{
\left(1-\lambda^{(3+2M)n}\kappa^{2Mn}\right)
       \nu_{\mathcal L}^{\mathrm{phys}}|_{\{Z,H\in p^n\}}.
}
\tag{37}
$$
这里 (37) 的补集还同时保留 $Z,H\in p^n$。
其系数对正 $n$ 为单位，说明真实输出补域不能被删掉。

若 Theta 对取另一深度 $r\ne n$，上述推前有额外的相对
$\kappa^{r-n}$ 缩放。(36) 不适用于这条非同步隐藏域。
R433 的独立两深度非零结论及 R432 的 Hadamard 补支仍须按
它们各自的原输入和输出完整运输。

## 10. 已付接口和剩余的同一中央问题

本篇已经给出新固定 ray、完整 degree7280 绝对平方、实际 degree1820
下降、两条固定残余来源的第一步 core、任意独立 sigma 测试下的
所有残余输出深度，以及原隐藏同深块的完整比例与补域。

原 $J'_S(0)=0$ 在 R430 中控制的是整个 $\mathcal K$ 的
$Y$-单位中央，乘任意完整 $X$ 测试。
(33) 则另带一个真正的残余双深条件，(32) 还显式保留 sigma
移动中心。不能因为输出 $Y,X$ 在该域都是单位，就把原完整中央零
直接分给它；也不能把 (37) 的单位补支忽略。
这些明确来源和域的中央关系是接续主目标的实际接口，主目标仍未完成。

## 依赖

- [R370：原 degree5 完整 core 与真实符号平方](R370-original-degree-five-core-and-common-infinite-six-phase-primes.md)。
- [R431：同一小核的完整 W core 与十三模 ray](R431-original-degree52-full-core-and-fixed-thirteen-ray.md)。
- [R435：原 R16 的双轴完整 core 与对角二挠不变性](R435-original-degree16-square-core-and-exact-two-axis-depth-transfer.md)。
- [R437：同一个独立 sigma 因子和原残余来源](R437-original-sigma-companion-cancellation-and-degree52-primitive.md)。
- [R432：原平衡表示和真实隐藏深度](R432-original-balanced-two-depth-source-and-three-actual-hadamard-tubes.md)。

