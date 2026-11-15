# R826 — 固定三条低权 CM 形式的四个 de Rham 槽与原权四分量的完整对角周期公式

日期：2026-11-15。**状态：下述固定角色、完整张量分解、坏处 Euler、四槽定位及第四槽的有限多项式 Abel–Jacobi 公式已证明。R829 已证明第3节当前同一 pr 拉回选定的对角 Chow 类为零，第四槽分子恒零；它不可能与 R814 的固定非零 canonical 类成非零比例。**

本篇给原三条
$\lambda_j=\eta_j^{-1}\psi_0^3$（$j=4,10,16$）
一个先于研究素数 $p$ 固定的权 $(2,2,2)$ 对角来源。
三条通常的 ordinary diagonal-cycle 公式读取三个不同的权二参考因子。
原 $\lambda_j$ 在全纯的第四槽，不能用其中任一单位根槽代替。

第四槽可以直接用 Besser 的完整 finite-polynomial 杯积计算；
不需要把 slope 恰为1的 CM 临界稳定化放进要求 slope 严格小于1的定理。
计算中保留两个真实原函数项、完整 Frobenius 归一及原对角类。

**后续范围修正：** [R829](R829-same-degeneracy-diagonal-chow-vanishing.md)由同一低层拉回及 cusp 基点兼容性证明当前选定类恒零。下述张量、Euler、杯积公式和独立的附录B保持有效；不得再把此同一向量的分子非零当作未付目标。

## 1. 三条固定权二角色及其全部有限数据

沿用 [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)。
令
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
\psi_0=\psi_{y^2=x^3+1}.
$$
$\psi_0$ 是原 type-$(1,0)$ 角色，采用 R806 的解析 CM type 和 reciprocity。
取 $\eta=\eta_{10}$，则
$$
\eta_j=\eta^{k_j},\qquad
(k_4,k_{10},k_{16})=(13,1,7),\qquad
\eta_j^3=\chi_{17}:=\psi_{17}/\psi_0 .
\tag{1}
$$
这些是固定十八阶角色，导子 $(34)$。
它们不是随 $p$ 重新选择的辅助字符。

定义
$$
\beta_j=\eta_j^{-2}\psi_0,\qquad
g_j=\theta(\beta_j),\qquad
f=\theta(\psi_{17}),\qquad
\gamma_j=\eta_j^{-7}\psi_0 .
\tag{2}
$$
这里 $\theta$ 为 Hecke theta series，首 Fourier 系数为1。
不与原 sigma 函数或原普通缩放常数混用。

写 $l_j=j-9$，$\vartheta_l(u)$ 是
$(u\bmod17)^{16l}$ 的同一 $\mu_{18}$ 提升。
R806 已付的有限角色相乘，给 $\beta_j\mathrm N^{-1/2}$ 的完整表：
$$
\begin{array}{c|c|c}
v&\text{单位上的角色}&\text{指定 uniformizer 值}\\ \hline
2&1&-1\text{ 于 }2\\
3&u\bmod\delta\in\{\pm1\}&+i\text{ 于 }\delta\\
17&\vartheta_{l_j}^{-2}&-1\text{ 于 }17 .
\end{array}
\tag{3}
$$
尤其二处的 cubic 角色确实抵消：
$\psi_0$ 的 $\operatorname{Teich}_{\mu_3}$ 与
$\eta_j^{-2}$ 的 $\operatorname{Teich}_{\mu_3}^{\,2}$ 相乘为1。
三处则没有抵消其单位角色；$\eta_j(\delta)=-1$ 的平方为1，
所以保留基角色的 $+i$。

因此
$$
\mathfrak f_{\beta_j}=(17\delta),\qquad
N(g_j)=|D_K|\mathrm N(17\delta)=2601,\qquad
\beta_j\beta_j^c=\mathrm N .
\tag{4}
$$
三个 $g_j$ 均为平凡 nebentypus 的固定权二 CM 新形式。
$f$ 的 level 是
$$
N(f)=10404=2^2\,3^2\,17^2 .
\tag{5}
$$
在2处，$g_j$ 的 primitive Euler 因子为
$(1+2^{\,1-2s})^{-1}$；其3、17处因子均为1。
$f$ 的2、3、17处 primitive 因子全为1。
这一区别在提升到共同 level 时不消失。

以下两个角色族也有准确导子 $(34\delta)$：
$$
\lambda_j=\eta_j^{-1}\psi_0^3,\qquad
\gamma_j=\eta_j^{-7}\psi_0.
\tag{6}
$$
$\lambda_j$ 是原 R814/R817/R818 的权四角色，未换来源。
$\gamma_j$ 的 unitary 有限表是
$$
\begin{array}{c|c|c}
2&\operatorname{Teich}_{\mu_3}^{-1}&-1\\
3&u\bmod\delta&-i\\
17&\vartheta_{l_j}^{-7}&-1 .
\end{array}
\tag{7}
$$
与 R757（《原 degree34 型零的完整六谱、三条九次环面线与中央质量》）
的完整角色定义相比，准确对应
$$
\gamma_4=\Psi^{(0)}_8,\qquad
\gamma_{10}=\Psi^{(0)}_2,\qquad
\gamma_{16}=\Psi^{(0)}_{14}.
\tag{8}
$$
(8) 使用 R757 式(14)、(15)：
三个十七处指数依次是 $-1,-7,5\bmod18$。
这是完整有限角色的比较，不仅比较好素数特征或角型。

## 2. 原八维张量的四个真实因子

用以下固定有序对：
$$
\begin{array}{c|c}
\ell&(j,k)\\ \hline
4&(10,16)\\
10&(16,4)\\
16&(4,10).
\end{array}
\qquad k_j-k_k\equiv-6\pmod {18}.
\tag{9}
$$
令 $g=g_j,h=g_k$。三个二次诱导的张量，按复共轭同时作用配对，
给精确恒等式
$$
\boxed{
AI(\psi_{17})\otimes AI(\beta_j)\otimes AI(\beta_k)
\simeq
AI(\lambda_\ell)\ \oplus\
\mathrm N\,AI(\gamma_\ell)\ \oplus\
\mathrm N\,AI(\psi_{17^3})\ \oplus\
\mathrm N\,AI(\psi_{17^5}).
}
\tag{10}
$$
这里 $\mathrm N$ 是实在的 Tate/范数因子，不能删除。

证明可在 $G_K$ 上逐行进行。三个未共轭因子的乘积为
$\eta^{3-2k_j-2k_k}\psi_0^3=\lambda_\ell$。
仅把第一、第二、第三个因子共轭，分别得到
$$
\mathrm N\gamma_\ell,\qquad
\mathrm N\psi_{17^3},\qquad
\mathrm N\psi_{17^5}.
\tag{11}
$$
例如后两式的 $\eta$ 指数为
$3+2(k_j-k_k)=9$ 和 $3-2(k_j-k_k)=15\bmod18$。
其余四行是这四行的共轭。由于所有局部角色是同一全局角色的限制，
该证明同时保留每一个坏地方。

特别 primitive 复 $L$ 函数准确分解为
$$
\boxed{
L(f,g_j,g_k,s)
=L(\lambda_\ell,s)
 L(\gamma_\ell,s-1)
 L(E_{17^3},s-1)
 L(E_{17^5},s-1).
}
\tag{12}
$$
四个右侧二维因子均在2、3、17处没有 inertia 不变量，
所以这些地方的四个 primitive Euler 因子都是1；
左侧不能另补 $g_j,g_k$ 在2处各自的好 Euler。
整个八维表示的有限导子为 $10404^4$，无穷因子为
$\Gamma_{\mathbf C}(s)\Gamma_{\mathbf C}(s-1)^3$。

R806 与 R757/R306 的原单位化 epsilon 表给
$$
\begin{array}{c|cccc}
&2&3&17&\infty\\ \hline
\lambda_\ell&1&-i&1&-i\\
\gamma_\ell,\ \psi_{17^3},\ \psi_{17^5}&1&-i&1&i .
\end{array}
\tag{13}
$$
四个诱导的局部 induction constants 的乘积为1。
因此三重积在每个有限地方的局部符号为 $+1$，无穷处为 $-1$；
它满足 Darmon–Rotger 的有限 split-trilinear 符号条件。

R818 已证 $L'(\lambda_\ell,2)\ne0$；
R757 式(39)、R307 的原完整参考公式给另外三个中心值非零。
于是 (12) 还证明这个固定低权三重积的复解析秩准确为1。
这一步仅为复 $L$ 函数陈述，不给对角类的 $p$-adic AJ 非零。

## 3. 同一个代数曲线、对角类及微分规范

置
$$
N=10404,\qquad X=X_1(N).
\tag{14}
$$
$f$ 取其原新形式，$g_j,g_k$ 通过
$$
\mathrm{pr}:X_1(10404)\longrightarrow X_1(2601),
\qquad (E,P)\longmapsto(E,4P)
$$
拉回。此映射泛型次数为12：固定一个 order2601 点，
其精确 order10404 原像由12个 primitive order4 分量给出。
固定这份旧空间嵌入，不任意改成别的2处 test vector。

计算时在固定 cusp 定义域取 $o=\infty$，$\Delta_X$ 为基于 $o$ 的
Gross–Kudla–Schoen 修正对角。若要求 $\mathbf Q$ 上的有理系数类，
可先取 $o$ 的 Galois 平均作为 degree1 零维循环；第5节证明本篇全纯槽
不受该基点替换影响。这里的定义域、投影及系数域均先于 $p$ 固定。
在足够大的代数系数域上，取 (10) 给出的真正 CM 幂等元，
记 $\Delta_\ell^{\mathrm{diag}}$ 为其 $\lambda_\ell$ 分量。
这是本篇的类；未将它命名为 R814 的 canonical 类。

所有微分用 q-展开规范
$$
\omega_x=x(q)\,\frac{dq}{q},\qquad x=f,g,h .
\tag{15}
$$
没有在 (15) 中附加 $2\pi i$ 或某个未显示的 CM 周期。
杯积配对取
$$
\langle u,v\rangle=\operatorname{tr}(u\cup v).
$$
在每份选定二维 CM 子空间上，$\eta_x^{\mathrm{ur}}$ 是单位根线中
满足
$$
\boxed{\langle\eta_x^{\mathrm{ur}},\omega_x\rangle=1}
\tag{16}
$$
的向量。顺序不能反写；相反顺序的值是 $-1$。
这是 DR 式(55)、(56) 的规范。
在 $g,h$ 的旧空间副本中，若下层按 (16) 规范，则
$$
\omega_x=\mathrm{pr}^*\omega_{x,\mathrm{new}},
\qquad
\eta_x^{\mathrm{ur}}
=\frac1{12}\mathrm{pr}^*\eta_{x,\mathrm{new}}^{\mathrm{ur}} .
\tag{17}
$$
这是杯积按映射次数放大的结果，不能把12约成“某个 period unit”。

取原已付 ordinary ray 上的 $p>17$，并固定原 CM 嵌入。
写
$$
\pi=\psi_0(\mathfrak p),\qquad
p=\pi\bar\pi,\qquad v_p(\pi)=1 .
$$
R806 的 $\eta_j(\mathfrak p)=-1$ 给
$$
\begin{array}{c|cc}
x&\alpha_x\text{（unit root）}&\beta_x\text{（slope1）}\\ \hline
f&-\bar\pi&-\pi\\
g,h&\bar\pi&\pi .
\end{array}
\tag{18}
$$
此处 $\beta_x$ 是 Hecke 根，不是 (2) 的 Hecke 角色。
CM 分解使全纯线本身成为 Frobenius 本征线：
$$
\varphi\omega_f=-\pi\omega_f,\qquad
\varphi\omega_g=\pi\omega_g,\qquad
\varphi\omega_h=\pi\omega_h .
\tag{19}
$$
系数扩域时用 Besser Definition2.3 的从 $\mathbf Q_p$ 基变换的线性
Frobenius，不能将系数共轭混入 (19)。

## 4. 三条 ordinary 公式实际读取哪些槽

$\mathrm{Fil}^2$ 在所选八维张量上恰有以下四条线：
$$
\begin{array}{c|c}
\text{de Rham 测试}&\text{(10) 中的来源}\\ \hline
\omega_f\otimes\omega_g\otimes\omega_h&AI(\lambda_\ell),\ \mathrm{Fil}^3\\
\eta_f^{\mathrm{ur}}\otimes\omega_g\otimes\omega_h&
\mathrm N\,AI(\gamma_\ell)\\
\omega_f\otimes\eta_g^{\mathrm{ur}}\otimes\omega_h&
\mathrm N\,AI(\psi_{17^3})\\
\omega_f\otimes\omega_g\otimes\eta_h^{\mathrm{ur}}&
\mathrm N\,AI(\psi_{17^5}).
\end{array}
\tag{20}
$$
这是逐 CM embedding 的 Hodge 分解：把一个全纯线改为单位根线，
就是把 (11) 的那个角色共轭。表中没有原 $E_{17}$ 参考因子。

DR Theorem5.1 在权 $(2,2,2)$ 的 $t=0$ 特化给三条准确公式
$$
\mathscr L_p^x(2,2,2)
=\frac{\mathcal E}{\mathcal E_0\mathcal E_1}
 AJ_p(\Delta_X)(\text{(20) 中以 }\eta_x^{\mathrm{ur}}\text{ 开的槽}),
\tag{21}
$$
这里三个 $\mathscr L_p^x$ 分别按循环顺序 $(f,g,h)$、$(g,h,f)$、
$(h,f,g)$ 定义，故搬回 (20) 的固定顺序不添 Koszul 负号。
它们使用 (14)–(17) 的实际 old test vectors 和 DR 的
Petersson/Serre-dual 规范。完整因子由 (18) 代入为
$$
\begin{split}
\mathcal E&=(1+\pi^{-1})(1+\bar\pi^{-1})^2
                     (1+\pi/\bar\pi^2),\\
\mathcal E_0&=1-\pi/\bar\pi,\qquad
\mathcal E_1=1-\bar\pi^{-2}.
\end{split}
\tag{22}
$$
对三个 dominant choices，这些因子相同。
它们均非零；例如 $\bar\pi=\pm1$ 会给
$\pi=\pm p$，与 $p>3$ 的 CM Weil 界冲突。

式(21)本身保留了所有 bad test vectors。
有限符号为 $+1$ 保证适当的 trilinear 向量存在，
却不证明任意所选的旧向量都有非零局部周期；
本篇不把17处三个 supercuspidal 输入的局部周期改成1。

表(20)已经说明：三条 ordinary 公式都不读取所需
$AI(\lambda_\ell)$ 的全纯槽。无论是否另外使用 rank-zero Selmer
定理，都不能用这三条公式直接判定第四槽。

## 5. 第四槽的完整 finite-polynomial 公式

取 $X$ 的一个足够小的 ordinary dagger 开子空间 $\mathcal W$，
带有从 $\mathbf Q_p$ 基变换的 Frobenius lift $\Phi$。
在 de Rham 上记其作用为 $\varphi$。
Besser (2.11) 的配对是先用唯一 Frobenius 相容的
开曲线到 proper 曲线的投影，再作 proper 杯积；本篇始终使用这一配对。

由 (19)，以下微分在 $\mathcal W$ 上 exact。
取过收敛函数 $G_g,G_h$，满足
$$
dG_g=(1-\pi^{-1}\Phi^*)\omega_g,\qquad
dG_h=(1-\pi^{-1}\Phi^*)\omega_h .
\tag{23}
$$
可把常数固定为在 cusp $\infty$ 的 q-展开常数为0。
因 $\Phi^*\omega_g=p\,\omega_{Vg}$，(23) 也准确写成
$$
\theta G_g=g-\bar\pi Vg,\qquad
\theta G_h=h-\bar\pi Vh,\qquad
\theta=q\,d/dq .
\tag{24}
$$
这是原 CM 临界稳定化的真实原函数；不以普通的
$\theta^{-1}g^{[p]}$ 代替。

定义完整的一阶形式
$$
\Xi_{g,h}
=G_g\omega_h-\pi^{-1}G_h\Phi^*\omega_g
=(G_gh-\bar\pi G_hVg)\frac{dq}{q}.
\tag{25}
$$

**定理。** 在上述同一曲线、同一向量和杯积规范下，
$$
\boxed{
AJ_p(\Delta_X)(\omega_f\otimes\omega_g\otimes\omega_h)
=
\frac{\langle\omega_f,[\Xi_{g,h}]\rangle}
     {1+\bar\pi/\pi^2}.
}
\tag{26}
$$
左侧就是 $\Delta_\ell^{\mathrm{diag}}$ 在 (20) 第一条线上的值。
分母的赋值为 $-2$，其逆的赋值为2，特别没有 exceptional zero。
这里没有把一个非零因子从别的 CM type 搬来。

### 5.1 未归一杯积与不可省的归一

对
$$
P_g(T)=P_h(T)=1-T/\pi
$$
使用 Besser Proposition2.2。(23) 给出两项
$(\omega_g,G_g)$、$(\omega_h,G_h)$ 的 finite-polynomial lifts，
其未归一杯积由 $(0,\Xi_{g,h})$ 代表。
卷积多项式为
$$
P_g*P_h=1-T/\pi^2.
$$
Besser (2.7) 明确规定自然映射 $\boldsymbol i$ 是 $P(\varphi)$，
而不是裸形式识别。因此真正的 de Rham 类为
$$
\boldsymbol i^{-1}
  (\widetilde\omega_g\cup\widetilde\omega_h)
=(1-\varphi/\pi^2)^{-1}[\Xi_{g,h}].
\tag{27}
$$
这个算子在相关开曲线 cohomology 上可逆：
proper $H^1$ 的 Frobenius 复权为1，
puncture 项为2，而 $\pi^2$ 的复绝对值为 $p$；
puncture 项若有同绝对值，其特征为 $p$ 乘单位根，
与 $\pi^2$ 不同，因为 $\pi/\bar\pi$ 不是单位根。
也可先限制到配对所需的 proper 本征分量，其特征为 $-\bar\pi$，
此时可逆性直接由 (26) 的非零分母给出。

Besser Proposition2.1 及其 §4 的 (4.2)–(4.3) 推导允许
**任意** $\eta\in H^1_{\mathrm{dR}}(X)$。取 $\eta=\omega_f$，
修正对角给
$$
AJ_p(\Delta_X)(\omega_f\omega_g\omega_h)
=\left\langle\omega_f,
 (1-\varphi/\pi^2)^{-1}[\Xi_{g,h}]\right\rangle .
\tag{28}
$$
部分对角/基点修正只包含两个 proper 全纯类的杯积，故全为零。
这里不是把只陈述 unit-root 情形的 Besser Theorem4.2
无条件推广；所用的是它证明之前的完整杯积恒等式。

### 5.2 原分母、常数及反对称的核对

Frobenius 相容性给
$$
\langle\varphi u,\varphi v\rangle=p\langle u,v\rangle .
$$
由 (19)，
$$
\langle\omega_f,\varphi v\rangle
=-\bar\pi\langle\omega_f,v\rangle .
\tag{29}
$$
把 (29) 代入 (28) 即得 (26)，特别分母是
$1+\bar\pi/\pi^2$，不能倒换为另一个普通位置的因子。

若改变 $G_g,G_h$ 的常数，(25) 只改变 proper 全纯类
$\omega_h,\Phi^*\omega_g$ 的线性组合；
它们与 $\omega_f$ 的杯积为零。因此 (26) 与这些常数选择无关。
改变修正对角的基点时，上述全纯杯积也说明本槽不变。

还有一个全来源的符号核对：
$$
\Xi_{g,h}+\Xi_{h,g}=d(G_gG_h).
\tag{30}
$$
故本槽在交换第二、第三个输入时反号，正好符合三个 $H^1$
因子的 Koszul 规则。特别 $g=h$ 时这一全纯槽为零。
本篇使用 (9) 的三个不同有序对，未由 (30) 把它们相认。

(25) 的第二项不能省掉。Besser 的 ordinary 化简只在
单位根测试和相应 ordinary projector 下得到；
全纯测试 (26) 不满足那一步的条件。
两项合在一起才是同一实际对角类。

## 6. 与完整 Bloch–Kato 公式及原 canonical 类的关系

本篇定理完全由第5节的已发表 Besser 杯积公式推出。下式(31)只核对新稿的完整向量范围，不以该预印本作为本篇证明输入。

Huang–Kazi–Marannino，arXiv:2601.05406v2，
Proposition3.7、Corollary5.6、Remark5.7 给的是
$$
\operatorname{ev}_{\omega_g\otimes\omega_h}
 \log_{\mathrm{BK}}(\operatorname{res}_p\kappa(f,g,h))
=\widetilde\omega-
 P_{gh}(\varphi)^{-1}P_{gh}(\varphi)\widetilde\omega
\tag{31}
$$
在完整的 $D_{\mathrm{dR}}(V_f^*(-1))$ 中的等式。
权 $(2,2,2)$ 的 balanced 条件使这里没有再丢一个 filtration 商。
因此 (31) 的原向量公式确实容许再与 $\omega_f$ 配对；
其后只与非临界 $\eta_f^\alpha$ 配对的标量定理不是全部内容。
本篇 (26) 在 CM 单根多项式下给出这一完整槽的具体两项表达。

(26) 的 Euler 分母恰与 R804 的局部式
$1+\bar\pi/\pi^2$ 相同。这与相同的一维 crystalline 参数相符，
但**不构成两个全局类相同的证明**。
R814 的类来自另一个先于 $p$ 固定的 generalized-Heegner 几何来源，
其几何维数、辅助 good pair、有限 test vector 和周期都已固定。
[R829](R829-same-degeneracy-diagonal-chow-vanishing.md)已证明，
本篇当前选定的同一 $\mathrm{pr}$ old 副本使整个对角投影为零。
因此这份(26)的分子恒零，与 R814 指定类的非零比例比较不可能；
它们不再是这份向量上的未决问题。
必须先更换实际2处退化向量，重新支付其全部 bad local test vectors 和周期，
再研究新对角类与 R814 指定类之间的真实全局比较及非零。
R817 的固定素数检测和 R818 的复解析秩一
分别保留原有效范围；不把任一条改写成跨 $p$ AJ 非零。
同样，这个新的低权几何呈示不自行给原
$J_S',J_T',J_U'$ 添加一个中央零条件。

## 7. 原文依据及复现范围

本篇没有新增数值计算。角色、级别和张量分解均由原完整有限数据
及逐角色乘法得到；新 AJ 公式是下面已发表杯积公式的直接推导。

- A. Besser, *On the regulator formulas of Bertolini, Darmon and Rotger*,
  Research in the Mathematical Sciences **3** (2016), article26：
  Proposition2.1、Proposition2.2、(2.7)、(2.11)–(2.13)，
  §4证明中的 (4.2)–(4.3)。
  <https://link.springer.com/article/10.1186/s40687-016-0073-x>
- H. Darmon, V. Rotger, *Diagonal cycles and Euler systems I:
  A p-adic Gross–Zagier formula*, Ann. Sci. Éc. Norm. Supér. **47**
  (2014), 779–832，式(6)–(8)、(55)–(56)、Theorem5.1。
  作者稿第46页的 Theorem5.1：
  <https://www.math.mcgill.ca/darmon/pub/Articles/Research/62.DR-Diagonal1/paper.pdf>
- T.-H. Huang, A. Kazi, L. Marannino, *New perspectives on p-adic
  regulator formulae*, arXiv:2601.05406v2，2026-06-17，
  Proposition3.7、Corollary5.6、Remark5.7（PDF第16–17页）。
  <https://arxiv.org/pdf/2601.05406v2>
- [R306](R306-jzero-three-sextic-original-local-data-and-full-weight-squares.md)、
  [R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)、
  [R757](R757-original-type-zero-six-spectrum-and-order-nine-lines.md)、
  [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)：
  同一 $\psi_0,\eta_j$ 的全2/3/17规范、参考中心值及有限角色。
- [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md)、
  [R817](R817-fixed-prime-original-negative-two-and-nonzero-fixed-cycles.md)、
  [R818](R818-original-three-weight-four-complex-analytic-rank-one.md)：
  原 fixed-cycle、fixed-prime 检测及复解析秩一；各自未付的跨 $p$ 门不变。

## 附录 A. 第四槽的原 CM companion、完整 q 系数及临界 cohomology 投影

本附录继续使用(14)–(25)的实际旧空间、周期和所选普通素位。
记 $\mathfrak f_\beta=(17\delta)$、$\alpha=\bar\pi$，
并把素于 $\mathfrak f_\beta$ 的非零整理想作为下面所有和的范围。
(23)的零常数原函数准确是
$$
\boxed{
G_j(q)=
 \sum_{\bar{\mathfrak p}\nmid\mathfrak a}
 \frac{\beta_j(\mathfrak a)}{\mathrm N\mathfrak a}
 q^{\mathrm N\mathfrak a}
 =
 \sum_{\bar{\mathfrak p}\nmid\mathfrak a}
 \eta_j(\mathfrak a)^{-2}
 \bar\psi_0(\mathfrak a)^{-1}q^{\mathrm N\mathfrak a}.
}
\tag{A1}
$$
确实，$\beta_j(\bar{\mathfrak p})=\bar\pi$，所以
$g_j-\bar\pi Vg_j$ 恰删去所有含 $\bar{\mathfrak p}$ 的整理想；
对余项施 $\theta^{-1}$ 就是除以其实际范数。
这也说明(A1)的系数在 p 处整，且
$$
UG_j=\bar\pi^{-1}G_j,\qquad
\theta G_j=g_j-\bar\pi Vg_j .
\tag{A2}
$$
它是这里的真实 weight-zero ordinary companion；不是只删去所有
$p$ 倍 Fourier 指标的 $p$-depletion。

(A1)也有不更改任何有限角色的经典权逼近。取
$k_r=2(p-1)p^r$，则 $12\mid k_r$，逐系数有
$$
\theta(\eta_j^{-2}\bar\psi_0^{\,k_r-1})^{\rm ord}
=
 \sum_{\bar{\mathfrak p}\nmid\mathfrak a}
 \eta_j(\mathfrak a)^{-2}\bar\psi_0(\mathfrak a)^{k_r-1}
 q^{\mathrm N\mathfrak a}
 \longrightarrow G_j .
\tag{A3}
$$
这里上标 ord 指实际删去 $\bar{\mathfrak p}$ 理想，保留的
$U$ 根是 $\bar\pi^{k_r-1}$。所有分母中的
$\bar\psi_0(\mathfrak a)$ 均为 p 单位，因此收敛逐项成立。
这些正权形式的二处角色仍平凡、三处单位角色仍为 sign，
十七处角色仍为 $\vartheta_{l_j}^{-2}$；
其导子仍是 $17\delta$，并使用(14)的同一旧空间拉回。
不通过某个未说明的有限角色变动把它变成原 $g_j$ 的权二普通支。
(A3)本身只用于核定系数与普通根；$G_j$ 的过收敛性已经由
(19)、(23)的 exactness 给出，不从“系数有极限”单独推过收敛。

设 $\Xi_{j,k}=\Xi_{g_j,g_k}$。它的完整 Fourier 系数为
$$
\begin{split}
[q^n]\frac{\Xi_{j,k}}{dq/q}
={}&\sum_{\substack{\mathrm N\mathfrak a+\mathrm N\mathfrak b=n\\
                    \bar{\mathfrak p}\nmid\mathfrak a}}
 \frac{\beta_j(\mathfrak a)\beta_k(\mathfrak b)}
      {\mathrm N\mathfrak a}\\
&-\bar\pi
 \sum_{\substack{\mathrm N\mathfrak a+p\,\mathrm N\mathfrak b=n\\
                    \bar{\mathfrak p}\nmid\mathfrak a}}
 \frac{\beta_k(\mathfrak a)\beta_j(\mathfrak b)}
      {\mathrm N\mathfrak a}.
\end{split}
\tag{A4}
$$
两项都含完整 $17\delta$ 条件，且仍在实际 level10404 旧向量上。
没有把第二项的 $p$ 倍指标吸入一个未经证明的标量。

还可精确定位(26)的投影。取 ordinary dagger cohomology 上的
$U=p\varphi^{-1}$；这是 normalized trace 与 Frobenius pullback
的关系，与权二 q 展开中的 $U$ 规范相同。
令 $\mathscr C_f(v)=\langle\omega_f,v\rangle$，由(29)有
$$
\boxed{\mathscr C_f(Uv)=-\pi\,\mathscr C_f(v).}
\tag{A5}
$$
因此第四槽在**形式的 $U$ 算子**上读取 slope1 的临界分量，
虽然在 proper cohomology 的 $\varphi$ 上读取 unit-root 分量。
二者的算子差一个 $p\varphi^{-1}$，不能混淆。
特别，直接用 ordinary-forms projector 先替换(A4)，会丢掉
(A5)所读的分量。这是必须保(25)两项的另一个准确说明。

## 附录 B. 原权四 Katz 支就是一个临界斜率 L 函数的中心首导数

以下是同一原 $\lambda_j$ 的单形式公式，不把它自动等同于
(26)的对角类。令
$$
F_j=\theta(\lambda_j),\qquad
\lambda_j=\eta_j^{-1}\psi_0^3,\qquad
\nu_j=\eta_j\bar\psi_0^3\mathrm N^{-1}.
\tag{B1}
$$
它们正是 R806/R804 的原角色。$F_j$ 是 level10404、权四、
平凡 nebentypus 的固定形式。由于
$\overline{\lambda_j(\mathfrak a)}=\lambda_j(\bar{\mathfrak a})$，
其 Fourier 系数为实数；LLZ 的共轭形式 $\bar F_j$ 因而就是 $F_j$。
在当前普通位的 Hecke 根为
$-\bar\pi^3$ 与 $-\pi^3$，后者为 slope3 的临界根。

采用 Lei–Loeffler–Zerbes（下简称 LLZ）§1.3 的 Artin 规范：
uniformizer 送至 arithmetic Frobenius 的逆。
于是他们附于 $\lambda_j$ 的一维 p-adic 表示是
$$
\rho_j=\widehat{\lambda_j}^{-1},\qquad
\rho_j^\iota=\widehat{\lambda_j^c}^{-1}.
\tag{B2}
$$
取 LLZ Lemma2.26 的 de Rham 同构、Betti 基 $\gamma_j$ 与微分基
$\omega_{\lambda_j}$；这些选择在本附录固定不变。
保持其实际非零 crystalline 比较周期
$$
\Omega_{j,p}^{\iota}
=\frac{\iota\gamma_j}{\iota\omega_{\lambda_j}} .
\tag{B3}
$$
这里包含所选 Artin/CM 基的全部比较，不把(B3)改成1，
也不凭 weight 相同将它认作原物理 $\Omega_p$。
Tate 因子的识别准确沿 LLZ Theorem3.2 的证明：
$t^{2-k}e_{k-2}$ 送至1，且本篇 $k=4$。

在完整模数 $\mathfrak f=(34\delta)$ 上，
LLZ Proposition2.22 的椭圆单位测度是 de Shalit II.4.14 的
正 Coleman 测度。取与 R804(10)相同的正规范后，它就是
$\mathcal K_{\mathfrak f}^{\rm prim}$；
原三个角色在2、3、17均真正分歧，故没有额外的 tame Euler。
辅助理想 $(5)$ 的平滑在 R804 中已按
$25-\nu_j((5))=30$ 除去；这里没有再乘一个30或18。
LLZ 所要求的 $\mathfrak f=\bar{\mathfrak f}$、
$\mathcal O_K^\times\cap(1+\mathfrak f)=\{1\}$、
最小正整数至少5均由该原模数满足。

令 $L^{\gamma_j}_{p,\mathrm{crit}}(F_j)$ 为 LLZ Definition3.3
在(B3)规范下的 Kato 临界斜率函数。为避免把两种 $\delta$ 混写，
以 $\epsilon_{\mathrm{cyc}}$ 表示 LLZ Lemma2.18 的 order2 群元；
它在 cyclotomic 塔上作用为 $-1$，不是 CM uniformizer $1+2\omega$。
对任意 cyclotomic character $\vartheta$，
LLZ Theorem3.2 的证明逐项给
$$
\begin{split}
L^{\gamma_j}_{p,\mathrm{crit}}(F_j)(\vartheta)
={}&\vartheta(\epsilon_{\mathrm{cyc}})
  (\ell_0\ell_1\ell_2)(\vartheta)\,\Omega_{j,p}^{\iota}\\
&\qquad\cdot
 \mathcal K_{\mathfrak f}^{\rm prim}
       \big((\chi_{\mathrm{cyc}}^2\rho_j^\iota)^{-1}\vartheta\big).
\end{split}
\tag{B4}
$$
这里 $(-1)^{k-2}=1$。本式引用的是该证明中保留
$\rho_j^\iota$ 的完整公式；不用把其末行省略上标的印刷写法
误读为另一个普通 CM type。

在固定 odd 分支取
$$
\vartheta_s=\chi_{\mathrm{cyc}}\,
              \langle\chi_{\mathrm{cyc}}\rangle^s ,
\qquad s\text{ 在 }0\text{ 附近}.
$$
由(B2)，Katz 参数准确为
$$
(\chi_{\mathrm{cyc}}^2\rho_j^\iota)^{-1}\vartheta_s
 =\widehat{\lambda_j^c}\,\chi_{\mathrm{cyc}}^{-1}
           \langle\chi_{\mathrm{cyc}}\rangle^s
 =\widehat\nu_j\langle\mathrm N\rangle^s .
\tag{B5}
$$
这是同一个原 finite $\eta_j$，没有先作裸共轭再漏掉普通地点。
同时
$\vartheta_s(\epsilon_{\mathrm{cyc}})=-1$，
而 $\ell_i=\log[\gamma]/\log\chi_{\mathrm{cyc}}(\gamma)-i$ 给
$(\ell_0\ell_1\ell_2)(\vartheta_s)=(1+s)s(s-1)$。
所以得到完整的原局部 germ
$$
\boxed{
L^{\gamma_j}_{p,\mathrm{crit}}(F_j)(\vartheta_s)
=\Omega_{j,p}^{\iota}\,s(1-s^2)\,
 \mathcal K_{\mathfrak f}^{\rm prim}
       (\widehat\nu_j\langle\mathrm N\rangle^s).
}
\tag{B6}
$$
特别，按这个 $s$ 坐标求导，
$$
\boxed{
\left.\frac{d}{ds}
 L^{\gamma_j}_{p,\mathrm{crit}}(F_j)(\vartheta_s)\right|_{s=0}
=\Omega_{j,p}^{\iota}\,
 34^2c_j\theta^9\Omega_p\,I_{j,-2,p}^{\,2}.
}
\tag{B7}
$$
此处 $\theta=17^{1/6}$，$c_j$ 和 $I_{j,-2,p}$ 完整沿 R806(27)、(32)。
若以 $x=\log(\vartheta_s(\gamma)/\chi_{\mathrm{cyc}}(\gamma))
=s\log\chi_{\mathrm{cyc}}(\gamma)$ 为坐标，则
$\frac{d}{dx}=(\log\chi_{\mathrm{cyc}}(\gamma))^{-1}\frac{d}{ds}$。
(B7)固定使用 $s$，没有隐藏该导数倍率。

因此这个固定权四形式的临界函数在中心已有一个强制零，
且它的阶数准确为
$$
\operatorname{ord}_{s=0}L^{\gamma_j}_{p,\mathrm{crit}}
=1+\operatorname{ord}_{s=0}
   \mathcal K_{\mathfrak f}^{\rm prim}
       (\widehat\nu_j\langle\mathrm N\rangle^s).
\tag{B8}
$$
若 germ 恒零，双方按无穷阶理解。
所以“该临界中心恰为 simple zero”当且仅当原 $I_j\ne0$；
没有从整个 Iwasawa 函数非零推固定值非零。
R817 的原固定素数7993已经支付三个 $I_j$ 均非零，
故(B8)在该固定检测处给三条真实 simple zero；
它不把这个结论推广到全部或无穷多个研究素数。

(B7)还与 R804 的原对数规范逐项相容：
$$
\boxed{
\log_j(\operatorname{loc}_{\mathfrak p}z_j)
=-\frac{\Omega_{p,0}^3}{\sqrt{17}\,\Omega_{j,p}^{\iota}}\,
  \frac{1+\pi/\bar\pi^2}{1+\bar\pi/\pi^2}\,
 \left.\frac{d}{ds}
 L^{\gamma_j}_{p,\mathrm{crit}}(F_j)(\vartheta_s)\right|_{s=0}.
}
\tag{B9}
$$
$\sqrt{17}$、原 local Euler 的方向、固定全局 $z_j$ 均未变化。

(B4)–(B9)涉及权四 $F_j$ 的 slope3 Kato 函数。
(A5)涉及权二 $f=\theta(\psi_{17})$ 的 slope1 cohomology 投影。
这两个真实对象不能仅因都称“critical”就相认。
要从(A4)的第四槽推出(B7)，仍需正文§6所列的实际全局类比较。
LLZ Theorem3.4 把 Kato 版本与 modular-symbol 版本比较到两个
非零 scalar（每个 parity 各一个）；本篇没有因此为未规范的
modular-symbol 函数赋上(B7)的绝对常数。

**附录的原文依据。**
A. Lei, D. Loeffler, S. L. Zerbes,
*Critical slope p-adic L-functions of CM modular forms*，
Israel Journal of Mathematics **198** (2013), 261–282，
[已发表版本](https://link.springer.com/article/10.1007/s11856-013-0020-0)，
[作者已接受稿](https://wrap.warwick.ac.uk/id/eprint/58879/1/WRAP_Loeffler_cmcritical.pdf)。
§1.2–1.3、Proposition2.22、Lemma2.26、Theorem2.28、
Lemma2.18、Theorem3.2及其证明、Definition3.3、Theorem3.4。
<https://arxiv.org/pdf/1112.5579>
本附录没有新增数值计算；(A1)–(A5)、(B5)–(B9)分别是完整
q 展开、Frobenius 对偶和该原文公式在本篇固定角色上的直接推导。
