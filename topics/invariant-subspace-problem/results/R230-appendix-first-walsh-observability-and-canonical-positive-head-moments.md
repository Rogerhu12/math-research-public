# R230 附录：一次 Walsh 的实际收缩观测与正密度全头矩约束

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065；主会话全文复核，central_review 独立核选择器、符号、常数及头矩代表；AI-assisted，GPT-6 Astra Pro。

**状态：以下观测界、准确矩代表及真湮灭者的高次数比例均完整证明。**
本稿首先构造原代数内的收缩 Cayley 测试，对全部复一次 Walsh 向量给出不依位置和位数的观测常数。随后将同一选择器用于真实正密度的准确有限头矩代表，得到
$$
\|v_m\|\le145\,\operatorname{Tr}\rho
+73\,\|P_{\ge2}v_m\|.
$$
若 $\rho$ 是非零正慢理想湮灭者，则 $\|v_m\|\to\infty$，
所以二次及以上 Walsh 分量的范数也趋于无穷，并至少占整体范数的 $1/73$。
这是对原正密度的具体约束，不是对某个固定非湮灭测试态的反例分析。

本稿不证明任意高次数部分可控，不给一般正常见证的不存在性，也不完成普通 ISP。

## 1. 原模型与同一个真实有限头

使用原 Haar 空间、真空 $\Omega=1$、反射共轭 $C$ 和实际
$$
A=d_0N_0,\qquad
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
E_j=|1\rangle\langle0|,\qquad
0<\eta_j\le e^{-770\,16^j},\quad\|N_j\|\le1.
\tag{1.1}
$$
记
$$
\theta_{j,m}=\prod_{s=j}^{m-1}\eta_s,\qquad j<m.
$$
在同一个前 $m$ 位头上定义
$$
N_j^{[m]}=
\sum_{k=j}^{m-1}
\left(\prod_{s=j}^{k-1}\eta_s\right)
E_j^*\cdots E_{k-1}^*E_k,
\qquad 0\le j<m,
$$
$$
A_{<m}=d_0N_0^{[m]}.
\tag{1.2}
$$
所有头外坐标取恒等扩张。
有限次实际递推准确给
$$
N_j-N_j^{[m]}
=\theta_{j,m}E_j^*\cdots E_{m-1}^*N_m,
$$
$$
\|N_j-N_j^{[m]}\|\le\theta_{j,m},\qquad
a_m^{\rm car}:=\|A-A_{<m}\|
=d_0\theta_{0,m}
\le d_0e^{-(770/15)(16^m-1)}.
\tag{1.3}
$$
最后的准确范数来自不交张量因子范数为1；
仅使用上界也足以完成全文。

有限头递推还给
$$
(N_j^{[m]})^2
=\eta_jI_j\otimes N_{j+1}^{[m]}
\quad(j<m-1),\qquad
(N_{m-1}^{[m]})^2=0.
$$
因此这些 $N_j^{[m]}$ 都是 $A_{<m}$ 的多项式并且两两交换。
其物理 $2\times2$ 块有单位下左角、上右角范数小于1，
所以 $\|N_j^{[m]}\|=1$。

定义完整和有限头 Cayley 元
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
V_j^{[m]}=(I-N_j^{[m]})(I+N_j^{[m]})^{-1},
$$
以及纯单个位矩阵
$$
D_j=I-2E_j.
\tag{1.4}
$$

### 1.1 准确源、对称性、增生性与局部差

上述两类 $V$ 都为 $C$ 对称；有限头版本使用头反射共轭。
有限头这一点可直接归纳：头反射在每位翻转 $e_0,e_1$ 并复共轭，
将 $(N_j^{[m]})^*$ 的两个物理块交换；由下一尾块的 $C$ 对称性，
得到 $C(N_j^{[m]})^*C=N_j^{[m]}$，末位 $E_{m-1}$ 为起点。
交换的多项式、逆及 Cayley 元继承同一对称性。
从 $N_j(\Omega_j+\chi_j)=\Omega_j-\chi_j$
（允许任意其余尾向量）直接得到
$$
V_j(\Omega_j\otimes h)=\chi_j\otimes h.
$$
同一式对 $N_j^{[m]}$ 成立。
按物理位从大到小使用，得到准确的完整有限列
$$
\boxed{
V_F\Omega=\chi_F,\qquad
V_F^{[m]}\Omega=\chi_F
\quad(F\subseteq[0,m)).
}
\tag{1.5}
$$
这与 [R253 §1](R253-positive-tail-partial-traces-and-dyadic-phase-product-elimination.md)
的实际 $V_F\Omega=\chi_F$ 一致，不是仅凭循环性作逼近。

若 $N$ 为收缩且 $I+N$ 可逆，
$$
\operatorname{Re}\bigl((I-N)(I+N)^{-1}\bigr)
=(I+N^*)^{-1}(I-N^*N)(I+N)^{-1}\ge0.
\tag{1.6}
$$
故所有 $V_j,V_j^{[m]},D_j$ 都增生。

因 $N_j^2=\eta_jN_{j+1}$，以及有限头同一递推，
$$
\|(I+N_j)^{-1}\|,\ \|(I+N_j^{[m]})^{-1}\|
\le\frac2{1-\eta_j}\le3.
$$
预解恒等式、$V=2(I+N)^{-1}-I$ 给
$$
\boxed{
\|V_j-D_j\|,\ \|V_j^{[m]}-D_j\|\le18\eta_j,\qquad
\|V_j-V_j^{[m]}\|\le18\theta_{j,m}.
}
\tag{1.7}
$$
第一项可取得更小常数，18便于统一。
由于 $\|D_j\|=1+\sqrt2$，原 $\eta_j$ 极小，
$$
\|V_j\|,\ \|V_j^{[m]}\|<3.
\tag{1.8}
$$
这些都是实际全算子范数界。

## 2. 正一次向量的纯收缩观测

先取非空有限位集 $J$ 和实数 $w_j\ge0$，并令
$$
w=\sum_{j\in J}w_j\chi_j,\qquad
B=\|w\|=\left(\sum_jw_j^2\right)^{1/2}>0,\qquad
L_0=\sum_{j\in J}w_jD_j.
$$
$L_0$ 增生，且
$$
L_0\Omega=w,\qquad L_0^*\Omega=-w.
\tag{2.1}
$$
逐个纯位的准确式 $D_j^2\Omega=2\chi_j-\Omega$ 和不交列 (1.5) 给
$$
L_0^2\Omega
=-B^2\Omega+2\sum_jw_j^2\chi_j
+2\sum_{j<k}w_jw_k\chi_{\{j,k\}},
$$
$$
\|L_0^2\Omega\|^2
=3B^4+2\sum_jw_j^4\le5B^4.
\tag{2.2}
$$

取
$$
t=\frac1{2\sqrt5 B},\qquad
R_0=(I-tL_0)(I+tL_0)^{-1},\qquad
u=(I+tL_0)^{-1}\Omega.
\tag{2.3}
$$
增生性给 $\|R_0\|\le1$、$\|(I+tL_0)^{-1}\|\le1$。
具体地，增生 Laplace 积分给预解的收缩性，而
$$
I-R_0^*R_0
=4t(I+tL_0^*)^{-1}(\operatorname{Re}L_0)(I+tL_0)^{-1}\ge0.
$$
所有物理矩阵与向量均为实，故 $\langle u,\Omega\rangle$ 为实。
由 (2.1) 和 $u+tL_0u=\Omega$，
$$
\langle R_0w,\Omega\rangle
=\frac2t(1-\langle u,\Omega\rangle).
\tag{2.4}
$$
又因 $\|u\|\le1$，
$$
2(1-\langle u,\Omega\rangle)\ge\|\Omega-u\|^2.
$$
准确二阶预解展开及 (2.2) 给
$$
u=\Omega-tw+t^2(I+tL_0)^{-1}L_0^2\Omega,
\qquad
\|\Omega-u\|\ge tB-t^2\sqrt5 B^2=\frac{tB}{2}.
$$
代入 (2.4)，得到
$$
\boxed{
\langle R_0w,\Omega\rangle
\ge\frac{B}{8\sqrt5}.
}
\tag{2.5}
$$

### 2.1 一次列的符号与未选位置

令 $a=\sum_jw_j$。因为 $L_0=aI-2\sum_jw_jE_j$，
有限幂零指数和增生预解的 Laplace 积分给
$$
u=\int_0^\infty
e^{-s(1+ta)}
\prod_{j\in J}(I+2tsw_jE_j)\Omega\,ds.
\tag{2.6}
$$
此积分按范数收敛；也可展开有限幂零多项式后逐项积分。

逐位有
$$
(I+2tsw_jE_j)\Omega_j
=(1+tsw_j)\Omega_j-tsw_j\chi_j.
$$
所以 $R_0\Omega=2u-\Omega$ 的每个一次 Walsh 系数在 $J$ 上为非正实数，
在 $J$ 外准确为零。
由于 $C\chi_j=-\chi_j$，对任意复一次向量
$b=\sum b_j\chi_j$，
$$
\langle R_0b,\Omega\rangle
=\sum_{j\in J} b_j d_j,\qquad d_j\ge0,
\tag{2.7}
$$
其中 $d_j$ 是 $R_0\Omega$ 第 $j$ 个一次系数的相反数。
这里使用纯矩阵的 $C$ 对称性，不将 $D_j$ 当成实际交换子。

## 3. 任意复一次向量的实际收缩选择器

取有限一次向量
$$
b=\sum_jb_j\chi_j,\qquad B_{\rm all}=\|b\|>0.
$$
把各系数的实部正负、虚部正负分为四个非负实向量。
四者的平方范数之和为 $B_{\rm all}^2$，
所以可选其中一个 w，使
$$
\|w\|\ge B_{\rm all}/2.
\tag{3.1}
$$
其支撑为 $J$，存在 $\zeta\in\{1,-1,i,-i\}$，
使 $w_j=\operatorname{Re}(\overline\zeta b_j)>0$ 对 $j\in J$ 成立。

按第2节用这个 w 构造 $R_0$。
未选位置的一次系数为零，选中位置的符号同向，
所以 (2.5)、(2.7) 给
$$
|\langle R_0b,\Omega\rangle|
\ge\operatorname{Re}\bigl(\overline\zeta
             \langle R_0b,\Omega\rangle\bigr)
\ge\frac{B_{\rm all}}{16\sqrt5}.
\tag{3.2}
$$

现在把 $L_0$ 替换为下列两种之一：
$$
L=\sum_{j\in J}w_jV_j
\quad\text{（完整实际版本）},
$$
或在 $J\subseteq[0,m)$ 时取
$$
L=\sum_{j\in J}w_jV_j^{[m]}
\quad\text{（同一个有限头版本）}.
$$
两者都增生、交换，且为各自代数中的有界元。令
$$
R=(I-tL)(I+tL)^{-1}.
\tag{3.3}
$$
增生性给 $\|R\|\le1$。
完整版本的 $R\in\mathcal A\subset A'$，
有限头版本的 $R\in\mathcal A_m:=\mathbb C[A_{<m}]$。
例如可用范数收敛的增生 Laplace 积分证明逆仍在相应范数闭代数中。

记
$$
E_\eta=\left(\sum_{j\ge0}\eta_j^2\right)^{1/2}.
$$
由 $16^j\ge j+1$，
$$
E_\eta\le2e^{-770}<1/576.
\tag{3.4}
$$
(1.7)、Cauchy--Schwarz 及两个增生预解的收缩性给
$$
\|L-L_0\|\le18\|w\|E_\eta,\qquad
\|R-R_0\|\le2t\|L-L_0\|
\le\frac{18}{\sqrt5}E_\eta.
$$
因此由 (3.2)--(3.4)，
$$
\boxed{
|\langle Rb,\Omega\rangle|
\ge\frac{\|b\|}{32\sqrt5},
\qquad \|R\|\le1.
}
\tag{3.5}
$$
常数不依位数、位置、复相位或系数的 $\ell^1$ 范数。

### 3.1 统一一次观测常数及稳健余项

记
$$
\Phi_v(F)=\langle Fv,\Omega\rangle.
$$
在完整实际代数中，任意有限一次向量
$v=b_0\Omega+b$ 满足
$$
\boxed{
\|v\|\le145\,\|\Phi_v|_{A'}\|.
}
\tag{3.6}
$$
同一式在前 $m$ 位头中对 $\mathcal A_m$ 成立。

确实，若右侧泛函范数为 $K$，取恒等测试得 $|b_0|\le K$。
对 (3.5) 的收缩 $R$，
$$
|\Phi_b(R)|\le|\Phi_v(R)|+|b_0|\,|\langle R\Omega,\Omega\rangle|
\le2K.
$$
所以 $\|b\|\le64\sqrt5 K$，而
$1+64\sqrt5<145$，得到 (3.6)。

更一般，在同一个有限头中写
$$
v=b_0\Omega+b+w,\qquad
b\text{ 为一次 Walsh 向量},\qquad
w=P_{\ge2}v.
$$
同一测试给
$$
|\Phi_b(R)|\le2K+\|w\|,
$$
故
$$
\boxed{
\|v\|\le145K+73\|P_{\ge2}v\|.
}
\tag{3.7}
$$
这里用了 $1+32\sqrt5<73$。
因此本结论不需要 v 严格为一次，
也定量控制了它相对集中在常数及一次空间的情形。

## 4. 从原正密度定义准确的全有限头矩代表

令 $\rho\ge0$ 为原 $H$ 上的迹类算子，
$$
\phi(T)=\operatorname{Tr}(\rho T),\qquad
\tau=\operatorname{Tr}\rho>0.
$$
$\phi$ 在全部 $B(H)$ 上为正且 $\|\phi\|=\tau$。
这允许观测真实有限头矩阵，即使它们不属于 $A'$。

对每个 $m$，定义
$$
\boxed{
v_m=
\sum_{F\subseteq[0,m)}
(-1)^{|F|}\phi(V_F^{[m]})\,\chi_F
\in K_m\otimes\mathbb C\Omega_m.
}
\tag{4.1}
$$
这是 $\rho$ 的明确有限头变换，不依赖选择重构表或假设未知成本上界。

$\{V_F^{[m]}\}$ 都在 $\mathcal A_m$ 中，
并由 (1.5) 将真空准确送到一个正交基。
因此它们线性无关，且已经张成维数 $2^m$ 的有限头代数。
也可由 $A_{<m}$ 是全部内部权非零的满长幂零移位，
直接看出 $\dim\mathcal A_m=2^m$。

由于有限头 $C$ 对称性和 $C\chi_F=(-1)^{|F|}\chi_F$，
$$
\langle V_F^{[m]}v,\Omega\rangle
=B(v,V_F^{[m]}\Omega)
=(-1)^{|F|}\widehat v(F).
$$
代入 (4.1)，得到
$$
\boxed{
\langle Rv_m,\Omega\rangle=\phi(R)
\qquad(R\in\mathcal A_m).
}
\tag{4.2}
$$
其中符号 $(-1)^{|F|}$ 必须保留。
没有把 $V_F^{[m]}$ 当成正交 Walsh 点乘。

特别，
$$
\langle v_m,\Omega\rangle=\tau,\qquad
\|\Phi_{v_m}|_{\mathcal A_m}\|=\tau.
\tag{4.3}
$$
又由 (1.8)，
$$
\boxed{
\|v_m\|^2
=\sum_{F\subseteq[0,m)}|\phi(V_F^{[m]})|^2
\le\tau^2\sum_F9^{|F|}
=\tau^2\,10^m.
}
\tag{4.4}
$$
有限维数没有给一个与 m 无关的界；(4.4) 明确保留全部增长。

将 (3.7) 用于 (4.3)，立即得到对每个真实正密度、每个 m 都成立的
$$
\boxed{
\|v_m\|\le145\tau+73\|P_{\ge2}v_m\|.
}
\tag{4.5}
$$
这里的收缩测试在有限头代数中准确实现，
其配对等于 $\phi(R)$，所以只使用正密度的范数 $\tau$。
没有直接把有限头 $R$ 放入原慢理想湮灭式。

## 5. 真湮灭者的矩代表必发散

再假设
$$
\phi(SA')=0,
\qquad S=S_N\text{ 或 }S_Y,
$$
并使用原 S 在 H 上单射的已证事实。

对固定多项式 $p(t)=\sum p_jt^j$，令
$$
L_p=\sum_{j\ge1}j|p_j|d_0^{j-1}<\infty.
$$
$\|A\|,\|A_{<m}\|\le d_0$，故望远镜式给
$$
\|p(A)-p(A_{<m})\|
\le L_p a_m^{\rm car}.
$$
由 (4.2)，
$$
\boxed{
|\phi(p(A))-\langle p(A)v_m,\Omega\rangle|
\le L_p a_m^{\rm car}(\tau+\|v_m\|)
\le L_p a_m^{\rm car}\tau(1+10^{m/2})
\longrightarrow0.
}
\tag{5.1}
$$
这一步完整支付了 $\|v_m\|$ 乘实际头差，
不是只估计 $\phi$ 一侧，也没有对变化多项式免费使用固定 $L_p$。

若 $v_m$ 有有界子列，取弱极限 v。
(5.1) 给 $\phi(p(A))=\langle p(A)v,\Omega\rangle$ 对全部多项式成立，
再由范数稠密性延拓到 $\mathcal A$。
取 $SA^j$ 得
$$
0=\langle A^jSv,\Omega\rangle=B(Sv,A^j\Omega).
$$
真空循环性迫 $Sv=0$，S 单射迫 $v=0$，
但取恒等又给 $\tau=0$，矛盾。
因此
$$
\boxed{\|v_m\|\longrightarrow\infty.}
\tag{5.2}
$$

同时 (5.1) 对每个固定幂给有界的
$\langle A^jv_m,\Omega\rangle$。
由于 $(A^*)^j\Omega=CA^j\Omega$ 张成稠密子空间，
$$
\boxed{
v_m/\|v_m\|\rightharpoonup0.
}
\tag{5.3}
$$
均值始终为 (4.3) 的非零 $\tau$，不是目标泛函已经丢失的归零构造。

结合 (4.5)，得到本稿对真实湮灭密度的主要约束：
$$
\boxed{
\|P_{\ge2}v_m\|\longrightarrow\infty,\qquad
\liminf_{m\to\infty}
\frac{\|P_{\ge2}v_m\|}{\|v_m\|}
\ge\frac1{73}.
}
\tag{5.4}
$$
例如任何固定 $\delta<1/73$ 的相对集中条件
$\operatorname{dist}(v_m,\mathscr H_{\le1})\le\delta\|v_m\|$
都不能在无穷子列上成立。
这个断言比只排严格一次向量更稳健。

## 6. 与精确全行重构、尾擦除的识别

本节给有限秩 $\rho=\sum_i f_i\otimes f_i$ 的直接源解释。
取恒等系数表 $T_{i\ell}=\delta_{i\ell}$、源 $g_i=Cf_i$，
所以重构误差准确为零，不要求降秩。

对每个 m，按前 m 位 Walsh 基写
$$
Cf_i=\sum_{F\subseteq[0,m)}
\chi_F\otimes z_{F,i}^{(m)}.
$$
定义
$$
W_{F,i}^{(m)}
=I_{K_m}\otimes
|\Omega_m\rangle\langle C_mz_{F,i}^{(m)}|.
$$
于是
$$
\widetilde v_m
=\sum_{F,i} V_F\,W_{F,i}^{(m)}f_i
$$
是 [纯远尾擦除主文](R230-appendix-pure-tail-source-erasure-and-carry-controlled-aggregate-growth.md)
固定头有界乘子合并的实际版本。

将这里的完整 $V_F$ 换成同一个有限头 $V_F^{[m]}$，所得向量
$$
v_m'=\sum_{F,i}V_F^{[m]}W_{F,i}^{(m)}f_i
$$
准确等于 (4.1) 的 $v_m$。
确实，对每个 $R\in\mathcal A_m$，
$W_{F,i}^{(m)}$ 与 R 严格交换，
有限头 $C$ 对称性和上面的源展开给
$\langle Rv_m',\Omega\rangle=\phi(R)$；
(4.2) 的有限头唯一性便给 $v_m'=v_m$。

完整差也可逐项支付。
由 (1.7)--(1.8) 的乘积望远镜，
$$
\|V_F-V_F^{[m]}\|
\le18|F|3^{|F|-1}\eta_{m-1}
\le6m\,3^{|F|}\eta_{m-1}.
$$
而两次 Cauchy--Schwarz 给
$$
\sum_{F,i}3^{|F|}
 \|z_{F,i}^{(m)}\|\,\|f_i\|
\le10^{m/2}\tau.
$$
因此
$$
\boxed{
\|\widetilde v_m-v_m\|
\le6m\,\eta_{m-1}\,10^{m/2}\tau
\longrightarrow0.
}
\tag{6.1}
$$
于是 (5.2)--(5.4) 也传给这个明确的原实际擦除向量
$\widetilde v_m$。
虽然 $\widetilde v_m$ 自身可带尾 carry，
与有限头代表的范数差已经付清。

## 7. 任意纯尾源表的一次集中也被预算内排除

沿用纯远尾擦除主文的真实重构表，
令 $v_n\in K_{m_n}\otimes\mathbb C\Omega_{m_n}$ 为擦除向量、
$\varepsilon_n\to0$ 为重构误差，
$$
H_n=\sum_\ell\|z_{\ell,n}\|\,\|h_{\ell,n}\|.
$$
这里先只处理纯尾情形，不把一般固定头合并向量自动当成有限柱。

对第3节根据 $v_n$ 的一次分量构造的**完整实际**收缩 $R_n$，
取同一系数的头收缩 $R_n^{[m_n]}$。
由 (1.7) 及 $t=(2\sqrt5\|w\|)^{-1}$，
$$
\|R_n-R_n^{[m_n]}\|
\le
\frac{18}{\sqrt5}\sqrt{m_n}\,\eta_{m_n-1}
=:\delta_{m_n}^{\rm sel}.
\tag{7.1}
$$
若一次分量为零，不需要这个选择器。

每个尾擦除矩阵与头 $R_n^{[m_n]}$ 严格交换，
所以即使 $R_n$ 随 n 变化，准确误差仍为
$$
|\phi(R_n)-\langle R_nv_n,\Omega\rangle|
\le\sqrt\tau\,\varepsilon_n
+2\delta_{m_n}^{\rm sel}H_n.
\tag{7.2}
$$
这不是把固定多项式的收敛擅自用于变化测试。

按 §3.1 同样分离常数项、一次项和余项，得到
$$
\boxed{
\|v_n\|
\le145\bigl(\tau+\sqrt\tau\,\varepsilon_n
                 +\delta_{m_n}^{\rm sel}H_n\bigr)
+73\|P_{\ge2}v_n\|.
}
\tag{7.3}
$$
若
$$
\delta_{m_n}^{\rm sel}H_n\to0,
\tag{7.4}
$$
则也有原 $a_{m_n}^{\rm car}H_n\to0$。
擦除主文的发散结论因而适用，给出与 (5.4) 相同的
高次数发散和 $1/73$ 的渐近比例。

特别，$q_n=2^{m_n}$ 时，
$H_n\le\exp(O(q_n^3\log q_n))$ 足以支付 (7.4)，
因为这里用的是
$\eta_{m_n-1}\le e^{-(770/16)q_n^4}$。
本节没有假设或证明一般源表确有这个预算。

## 8. 范围及下一真实缺口

一次观测常数没有依赖有限柱维数，也没有将实际收缩条件
误作原标量多项式的 Schur 延拓。
它来自真实增生 Cayley 元、正一次列的明确符号、
以及两种实际 carry 的分别支付。

第4--6节直接使用原正密度的有限头矩。
正性用于 $\|\phi\|=\tau$，不是把一个未在 $A'$ 中的有限头投影
拿去测试慢理想。
慢湮灭式只在第5节通过固定实际多项式的合法极限进入。

当前得到的是：真见证的明确矩代表不能把发散几乎全部放在常数及一次层。
二次以上的复杂相消仍可能存在。
没有给该高次数部分的上界，也没有将本结论扩为所有固定次数、
所有一般右因子或普通 ISP 的完整答案。
