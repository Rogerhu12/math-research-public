# R735 — 两条原型五来源的完整 Schwartz、rank-one Katz 负一值与共同周期

日期：2026-11-15。**状态：已证明。**

本篇将 R732 的两条实际型五特征线准确识别为
$E_{289}:y^2=x^3+289$、$E_{83521}:y^2=x^3+83521$
的同一全权 theta 来源。完整的2、3、17处角色、Schwartz向量、半特征、
绝对 CM13 相位、全权范数、共同复/普通周期及负一单位域均保留。
两条曲线的解析秩一由严格有理区间证明。
原负一矩因此非零，并在同一 $E_1:y^2=x^3+1$ 的微分下，
分别等于**代数常数乘一次椭圆 logarithm，再除同一个 ordinary 周期**。

这一步与 R733 的对数独立性结合，支付 R734 实际两线组合的非消失。
原 paired-T 外部依旧给出相反补偿，未据此宣称固定 rank-two 主目标完成。

## 1. 来源、曲线与所证公式

固定
$$
K=\mathbf Q(\omega),\quad\omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad\operatorname{Im}\delta>0,\qquad
\theta=17^{1/6}>0 .
\tag{1}
$$
各 $p$ 处选与原题一致的代数嵌入。
记 $\psi_k$ 为
$$
E_k:y^2=x^3+17^k,\qquad k=2,4
$$
在解析微分 $dx/(2y)$ 上的 CM Hecke 角色，$\psi_0$ 对应 $E_1:y^2=x^3+1$。
以下 k 是幂指数，不将 $E_k$ 与曲线常数 k 混淆。
由 [R732](R732-original-type-five-full-cm13-and-two-eigenlines.md)，令
$$
D_{2,b}=D_{\omega,b},\qquad D_{4,b}=D_{-,b},\qquad b=17,
\tag{2}
$$
两来源均按首项 $z^5$ 规范。

令 $\Omega_{p,0}=\theta\Omega_p$，$\Omega_p$ 是原 $E_{17}$ 的周期；
令 $\nu_{D_{k,b}}$ 的 Amice 变换为
$D_{k,b}(\Omega_p\log(1+T))$，并置
$$
I_{k,p}=\int_{\mathbf Z_p^\times}x^{-1}\,d\nu_{D_{k,b}}(x).
\tag{3}
$$
不存在变量 $x\mapsto\theta x$ 的隐含替换；这是原同一个 $\mathbf Z_p$ 变量。
下文定义固定非零代数常数 $c_k$，并证明
$$
\boxed{
\mathcal L^{\rm prim}_{p,34\delta}(\bar\psi_k)
 =34c_k\theta^{11}\Omega_p I_{k,p}^{\,2}\ne0 .
}
\tag{4}
$$
该公式对原 ordinary ray 上全部好素数成立。
它是型 $(0,1)$ 的共轭 Katz 值，不是把裸复中央值当作非零。

## 2. 完整有限角色与合法全权

采用 R290 的加性角色及 Yang 极化：
$$
\psi_{\infty,\rm add}(x)=e^{2\pi ix},\qquad
\psi_{\ell,\rm add}(x)=e^{-2\pi i\{x\}_\ell},\qquad X=\mathbf Q\delta .
$$
Silverman–Stange §6 的完整六次剩余公式给
$$
\psi_k(\mathfrak q)
=-\left(\frac{4\cdot17^k}{\mathfrak q}\right)_6^{-1}\pi,\quad
\pi\equiv2\bmod3,\qquad
\frac{\psi_k}{\psi_0}=\left(\frac{17}{\cdot}\right)_6^{-k}.
\tag{5}
$$
因此并未根据一个好素理想的特征猜角色。

设 $\chi_k=\psi_k\mathrm N^{-1/2}$。其实际坏点表为
$$
\begin{array}{c|c|c}
v&\chi_{k,v}(u)\text{，u为单位}&\text{uniformizer值}\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)&-1\text{ 于 }2\\
3&u\bmod\delta\in\{\pm1\}&+i\text{ 于 }\delta\\
17&(u\bmod17)^{48k}&-1\text{ 于 }17 .
\end{array}
\tag{6}
$$
十七处幂的正号是 idèle 单位分量，与 (5) 的理想角色互逆。
理由与 R306 的完整主 idèle 推导相同：
17在 $\mathbf Q_2$ 是六次幂；
在 $\mathbf Q_3$ 是三次幂，其平方根给未分歧二次扭曲，
k为偶数时该扭曲消掉，故三处 uniformizer 保留基值 $+i$。
主 idèle 17 的积关系给十七处的 $-1$。
两条十七处角色均为非平凡三次角色。
所以
$$
\mathfrak f_{\psi_k}=(34\delta),\qquad
\mathrm N\mathfrak f_{\psi_k}=3468,\qquad N_{E_k}=10404.
\tag{7}
$$

正权取 $\Phi_{k,m}=\psi_k^{2m+1}$。当且仅当
$$
m\equiv5\bmod6
\tag{8}
$$
时，以下同一个有限来源适用：
$$
\begin{array}{c|c|c}
v&\chi_{k,m,v}(u)&\text{uniformizer值}\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)^{-1}&-1\\
3&u\bmod\delta&-i\\
17&(u\bmod17)^{-48k}&-1 .
\end{array}
\tag{9}
$$
这里 $\chi_{k,m}=\Phi_{k,m}\mathrm N^{-m-1/2}$。
二处、三处分别要求 $2m+1\equiv-1\bmod3,4$；
十七处再核 $(2m+1)48k\equiv-48k\bmod288$，共同类准确为 (8)。

在 R290 同一个 $\psi_K/2$ 规范，(9) 的 Yang dichotomy
$\epsilon(1/2,\chi_{k,m,v},\psi_{K,v}/2)\chi_{k,m,v}(\delta)$
在 $2,3,17,\infty$ 依次为 $+1,-1,-1,+1$。
十七处逆三次角色沿 $x+y\delta$ 的 x 纤维求和为
$$
\sum_{y:\,x+y\delta\ne0}(x+y\delta)^{48k}
 =\begin{cases}16,&x=0,\\-1,&x\ne0,\end{cases}
\tag{10}
$$
故完整加性 Gauss 和为 $+17$。
乘 uniformizer 的 $-1$ 后 epsilon为 $-1$，而
$\chi_{k,m,17}(\delta)=1$。
二、三处分别使用 R290 的 $\mathbf F_4$ Gauss 和2、
$\mathbf F_3$ 二次 Gauss 和 $i\sqrt3$。
因此所需 Hermitian 类仍准确为
$$
\boxed{\alpha=17,\qquad \mathcal G=|\delta^3\alpha|=51\sqrt3 .}
\tag{11}
$$
它不是从相同 theta 次数推测出来的。

## 3. 全部原 Schwartz 向量

### 3.1 十七处：完整奇三次向量

在原奇导子 lattice model
$e_a=\mathbf1_{a/17+\mathbf Z_{17}}$ 上，取
$$
g_0=2+4\delta\in\mathbf F_{289}^{\,1},\qquad
g_0^{18}=1,\qquad g_0^6=\omega .
$$
记 $\zeta_{17}=e^{2\pi i/17}$、$\sqrt{17}>0$。
原有限算子为
$$
W(x+y\delta)_{ab}
=-\frac{(y/17)}{\sqrt{17}}
 \zeta_{17}^{\,\frac3{2y}\{x(a^2+b^2)-2ab\}}\quad(y\ne0),
\quad W(1)=I,\quad W(-1)e_a=e_{-a}.
\tag{12}
$$
式 (12) 是 R290 从 Yang 的实际极化和 splitting 得到的原模型。
原 Hecke splitting 与 $\mu_4$ splitting 差一个二次环面角色。
由 Hilbert 90，(9) 对应 $g^{3k}$，故原不变向量需要
$$
\tau_k(g)=g^{9-3k},\qquad
\tau_2(g_0)=-\omega^2,\quad \tau_4(g_0)=-\omega .
\tag{13}
$$
不能漏掉9所代表的 quadratic splitting。

令
$$
\Pi_{\tau_k}=\frac1{18}\sum_{j=0}^{17}\tau_k(g_0)^{-j}W(g_0^j),
\qquad
f_k=18\sqrt{17}\,\Pi_{\tau_k}e_1 .
\tag{14}
$$
全环面的 character trace 给 $\operatorname{tr}\Pi_{\tau_k}=1$。
由 (12) 的有限商环运算，完整地有
$$
W(g_0)f_k=\tau_k(g_0)f_k,\qquad
f_k(-a)=-f_k(a),\qquad \overline{f_k(a)}=f_k(a),\qquad f_k(1)\ne0 .
\tag{15}
$$
因此 $f_k$ 是真实的实奇向量。
亦可分别从 $\overline{W(g)}=W(g^{-1})$、
$\tau_k(-1)=-1$ 和正交投影直接看出。
原完整平方范数准确为
$$
n_k:=\sum_{a=0}^{16}|f_k(a)|^2
 =18\sqrt{17}\,f_k(1)>0 .
\tag{16}
$$
这定义了固定可重算的正代数数；不将它规范成1。
取 $\phi_{17,k}=\sum_a f_k(a)e_a$。

(10)、(12)–(16) 在
$\mathbf Q(\zeta_{51})$ 中逐项进行，所有17个坐标与全部18个环面元都保留。
公开 producer 的28个精确断言包含非零投影、multiplicity、实奇性、完整范数、
两种三次角色的全 Gauss 和及下文绝对相位；不使用有限好素数猜测。

### 3.2 二处与三处

二处取
$$
e_j=\mathbf1_{j/2+2\mathbf Z_2},\quad
f_A=e_0-e_2,\quad f_B=e_1+e_3,\quad
t_-=\frac{1-\sqrt3}{\sqrt2},\qquad
\boxed{\phi_2=f_A+t_-f_B.}
\tag{17}
$$
R290 原旧矩阵在 $(f_A,f_B)$ 上为
$$
M_\omega^{\rm old}
=\frac{\omega^2}{\sqrt2}
 \begin{pmatrix}-\zeta_8&i\\i&i\zeta_8\end{pmatrix},
\quad
M_\omega^{\rm old}(1,t_-)^{\mathsf t}
=\omega(1,t_-)^{\mathsf t}.
$$
(9) 相对旧二处角色的 splitting 比在 $\omega$ 上为 $\omega^2$，
所以新矩阵 $\omega^2M_\omega^{\rm old}$ 准确固定 (17)。
对
$g_*=(-11+4\delta)/13$，该比为1，完整四陪集矩阵仍为
$$
\begin{pmatrix}0&0&-1&0\\0&1&0&0\\-1&0&0&0\\0&0&0&1\end{pmatrix}.
$$
$-1$ 也固定 (17)。
R290 的 $\mu_3,-1,g_*$ 拓扑生成整个 $K_2^1$ 的证明原样适用，
因此这里核定的是全部本地环面，而不是单个 good-prime 相位。
自对偶测度下
$$
\|\phi_2\|^2=1+t_-^2=3-\sqrt3.
\tag{18}
$$
三处 (9) 与 R290 完全相同，Yang 的原转模给
$$
\phi_3=\mathbf1_{3^{-1}\mathbf Z_3},\qquad \|\phi_3\|^2=3.
\tag{19}
$$
其他有限处为标准球。好分裂处未分歧参数虽随 m 变，
Yang Corollary 2.14 仍给同一球；未声称整个全局角色恒定。

## 4. 标准 degree34 下降及两条来源的准确识别

原有理支撑仍是 $n/102$。完整有限系数为
$$
a_{k,n}=v_2(n\bmod4)f_k(3n\bmod17),\qquad
v_2=(1,t_-,-1,t_-).
\tag{20}
$$
它为非零实奇序列，周期68，且
$$
(-1)^n a_{k,n+34}=-a_{k,n}.
\tag{21}
$$
故 R292 的完整半周期计算直接给
$$
\begin{aligned}
F_k(Z)&=\sum_{n\in\mathbf Z}a_{k,n}
 e^{\pi i(\delta/3)n^2/68+2\pi inZ},\\
F_k(Z+1)&=F_k(Z),\qquad
F_k(Z+s_0)=e^{-34\pi is_0-68\pi iZ}F_k(Z),\\
s_0&=(1-\omega)^{-1},\qquad\Lambda=\mathbf Z+s_0\mathbf Z .
\end{aligned}
\tag{22}
$$
所以
$$
S_{k,\Lambda}(Z)=e^{34\sqrt3\pi Z^2}F_k(Z)
$$
是同一标准 degree34 theta 截面，没有未指定的二挠 twist。
在实轴上它纯虚；整个 Fourier 序列非零，故截面非零。

几何 $\mu_3$ 算子的本地标签按原 R290/R297 约定是 $g=\omega^2$。
二处 (17) 在旧固定模型的相位为 $\omega^2$，
十七处 $\tau_k(g_0^{12})=1$；故
$$
S_{k,\Lambda}(\omega Z)=\omega^2S_{k,\Lambda}(Z),\qquad
S_{k,\Lambda}(-Z)=-S_{k,\Lambda}(Z).
\tag{23}
$$
因此它属于 R732 的整个型五空间，而不是型一奇块。

还须定实际 CM13 的绝对相位。
在与 R732 完全同一 whole degree34 trace 规范中，
$\gamma=4+\omega$ 的本地标签为
$$
g_{13}\bmod4=\omega^2,\qquad g_{13}\bmod17=g_0^{14}.
$$
原 S 的绝对 $N_{13}=-1$ 已由 R297/R732 全十三纤维支付；
其旧二处相位1、十七处相位 $\omega$，故共同全局因子准确为 $-\omega^2$。
该因子由同一完整 Heisenberg 交织和这个非零锚定标，
与所选截面无关。代入本篇全有限向量得到
$$
N_{13}S_{2,\Lambda}=(-\omega^2)\omega^2\tau_2(g_0)^{14}S_{2,\Lambda}
=-\omega^2S_{2,\Lambda},
$$
$$
N_{13}S_{4,\Lambda}=(-\omega^2)\omega^2\tau_4(g_0)^{14}S_{4,\Lambda}
=-S_{4,\Lambda}.
\tag{24}
$$
这使用的是已构造的**完整有限角色**；CM13 仅在 R732 两个已付的一维空间中
确定实际截面，不以一个 Hecke 特征识别整个未知角色。

令 $\Omega_0>0$ 使 $E_1$ 的格为 $\Omega_0\Lambda$，
$\varpi_0=s_0\Omega_0$ 为其固定 $\mathcal O_K$ 生成周期。
由 (23)、(24) 与 R732 的单重性，存在 $s_k\in i\mathbf R^\times$，
使
$$
\boxed{S_{k,\Lambda}(Z)=s_kD_{k,1}(\Omega_0Z).}
\tag{25}
$$
每条 $D_{k,1}$ 首项 $z^5$；(25) 的 $s_k$ 非零且尺度完全保留。

## 5. 全权平方与固定代数常数

原 Hermite 生成函数给
$$
\begin{aligned}
b_{k,m}
&=\sum_{n\in\mathbf Z}a_{k,n}
 H_m(\sqrt{51\sqrt3}\,n/102)
 e^{-\pi\sqrt3 n^2/204}\in\mathbf R,\\
\sum_{m\ge0}b_{k,m}T^m/m!
&=S_{k,\Lambda}(h_\infty T),\qquad
h_\infty=\frac{\sqrt{51\sqrt3}}{204\pi i}.
\end{aligned}
\tag{26}
$$
这里 $H_m$ 仍由
$\exp(xT-T^2/(8\pi))=\sum H_m(x)T^m/m!$ 定义。
(23) 说明只保 $m\equiv5\bmod6$。
设 $d_{k,m}=[z^m]D_{k,1}(z)$，则
$$
b_{k,m}=m!s_k(\Omega_0h_\infty)^m d_{k,m}.
\tag{27}
$$

原全局范数为
$$
\mathcal N_{k,m}
=\frac{3(3-\sqrt3)n_k}{\sqrt{102\sqrt3}}
 \frac{m!}{(4\pi)^m}.
$$
Yang 的原 $S_1=\{2,17\}$、$c(0)=17/27$、
类数一/范数一紧群体积比6都与 R290 相同。
因此对每个非负合法 m，
$$
\boxed{
L(\psi_k^{2m+1},m+1)
=C_k\frac{(4\pi)^m}{m!}b_{k,m}^2,\qquad
C_k=\frac{\pi\sqrt{102\sqrt3}}
 {17\sqrt3(3-\sqrt3)n_k}>0 .
}
\tag{28}
$$
式 (28) 是真实同一来源的实平方，有限范数没有被约成1。

由
$4\pi h_\infty^2=-\sqrt3/(204\pi)$ 及 m 为奇数，
令 $\varkappa_k=-C_ks_k^2/\Omega_0>0$，得到
$$
\frac{(2\pi/\sqrt3)^mL(\psi_k^{2m+1},m+1)}
 {m!\Omega_0^{2m+1}}
=\varkappa_k\,102^{-m}d_{k,m}^2 .
$$
再用 $s_0^{-2m}=-\omega^2\,3^m$（$m\equiv5\bmod6$），定义
$$
c_k=-\frac{\omega^2\varkappa_k}{s_0}
=34^5\,
 \frac{(2\pi/\sqrt3)^5L(\psi_k^{11},6)}
 {5!\varpi_0^{11}}\in\overline{\mathbf Q}^{\,\times}.
\tag{29}
$$
最后的代数性是 CM 临界值代数性；例如 BDP Proposition 2.11、
Theorem 2.12 所用的 period 规范给出它。
非零性由 (25)、(27)、$d_{k,5}=1$ 和 (28) 给出，
不由数值 L 估计给出。
于是全部合法权的准确共同公式为
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\psi_k^{2m+1},m+1)}
 {m!\varpi_0^{2m+1}}
=c_k\,34^{-m}d_{k,m}^2 .
}
\tag{30}
$$
$c_k$ 是固定代数数；不是一个随 p 改动的未知解析量。

## 6. 同一普通单位测度与负一 Katz 点

在原 ordinary 地点，取 $\Omega_{p,0}=\theta\Omega_p$，
并定义
$$
M_{k,m}=\int_{\mathbf Z_p}x^m\,d\nu_{D_{k,1}}(x)
=\Omega_{p,0}^m m!d_{k,m}.
\tag{31}
$$
$\nu_{D_{k,1}}$ 仍是整个原标准 theta 来源的有界测度。
正权角色为
$$
\nu_{k,m}=\psi_k^{m+1}\bar\psi_k^{-m},
\qquad m\equiv5\bmod6,\qquad
\nu_{k,m}\nu_{k,m}^c=\mathrm N .
\tag{32}
$$
其导子为 $34\delta$。记
$\alpha_k=\psi_k(\mathfrak p)$、
$\bar\alpha_k=\psi_k(\bar{\mathfrak p})$，
按原嵌入 $v_p(\alpha_k)=1,v_p(\bar\alpha_k)=0$。
BDP Theorem 3.1 / Proposition 3.5 的 primitive 插值准确为
$$
\begin{aligned}
\mathcal L^{\rm prim}_{p,34\delta}(\nu_{k,m})
={}&\Omega_{p,0}^{2m+1}m!\,
 \frac{(2\pi/\sqrt3)^mL(\psi_k^{2m+1},m+1)}
      {\varpi_0^{2m+1}}\\
&\quad\cdot
 \left(1-\frac{\alpha_k^m}{\bar\alpha_k^{m+1}}\right)^2\\
={}&c_k\Omega_{p,0}34^{-m}
 \left(1-\frac{\alpha_k^m}{\bar\alpha_k^{m+1}}\right)^2M_{k,m}^2 .
\end{aligned}
\tag{33}
$$
两个普通 Euler 因子
$1-\nu_{k,m}(\mathfrak p)/p$、
$1-\nu_{k,m}^{-1}(\bar{\mathfrak p})$
严格相同。二、三、十七处角色均分歧，primitive 公式没有另删坏点因子。

令 $m_r=-1+(p-1)p^r$。这些权保持 (8)，实趋无穷、p进趋 $-1$。
非单位部分的 $m_r$ 矩趋零，普通 Euler 减一也趋零，
单位部分则一致趋向原负一测试。
全部周期变指数已经在 $M_{k,m}$ 中，未对任意
$\mathbf C_p$ 单位进行未定义的指数延拓。
由 Katz 连续性，(33) 准确给
$$
\boxed{
\nu_{k,-1}=\bar\psi_k,\qquad
\mathcal L^{\rm prim}_{p,34\delta}(\bar\psi_k)
=34c_k\Omega_{p,0}
 \left(\int_{\mathbf Z_p^\times}x^{-1}\,d\nu_{D_{k,1}}\right)^2 .
}
\tag{34}
$$
一般负一 Mellin 变量 w 上同一分支还保
$34c_k\Omega_{p,0}\langle34\rangle^{-(p-1)w}J_k(w)^2$。

最后由 R732 的真正六次缩放
$$
D_{k,17}(z)=\theta^{-5}D_{k,1}(\theta z),\qquad
\nu_{D_{k,1}}=\theta^5\nu_{D_{k,17}},
\tag{35}
$$
回到 (3)，得到 (4) 的完整系数 $34c_k\theta^{11}\Omega_p$。
(35) 是同一个测度变量上的来源等式，不改变原单位域。

## 7. 解析秩一的严格有理证明

对 (6) 的权一角色，
$\epsilon(1/2,\chi_{k,v},\psi_{K,v}/2)$
在 $2,3,17,\infty$ 依次为
$$
+1,\quad-i,\quad-1,\quad i .
$$
十七处仍用 (10)，三处 uniformizer 平方为 $-1$。
故两个全 root number 都为 $-1$。
结合完整导子 (7)，令 $c=2\pi/102=\pi/51$，
权二 functional equation 的积分形式给
$$
L'(E_k,1)=2\sum_{n\ge1}\frac{a_n(E_k)}nE_1(cn),
\qquad E_1(x)=\int_x^\infty e^{-t}\frac{dt}{t}.
\tag{36}
$$
不通过数据库解析秩或浮点近零判断来证明非消失。

脚本从两个原方程逐个计数所有 $\ell\le512$ 的好素数，
二、三、十七处为加性约化、$a_\ell=0$；
再用实际乘法性和 $a_{\ell^{r+1}}=a_\ell a_{\ell^r}-\ell a_{\ell^{r-1}}$
恢复全部 $a_n,n\le512$。
Hasse 界给 $|a_n|\le d(n)\sqrt n\le2n$。

全部区间使用有理数：
$\pi$ 用32项 Machin 交错级数；
$\log$ 先缩到 $[1,2]$，用24项 atanh 正级数及其几何尾；
Euler 常数用 $H_{128}$ 的 Euler–Maclaurin 交错积分余项；
$E_1(x)$ 用
$$
E_1(x)=-\gamma_{\rm Euler}-\log x+
 \sum_{r=1}^{144}\frac{(-1)^{r+1}x^r}{r\,r!}
+\text{下一项所界定的交错尾}.
$$
这里全部 $x\le512\pi/51<145$，从所截处起项绝对值严格下降。
每个中间 $E_1$ 区间向外舍入到 $10^{-18}\mathbf Z$，
只增大误差、不作浮点替代。
若 $c_-$ 是 c 的有理下界、$z=(1+c_-)^{-1}$，
完整 $n>512$ 尾严格不超过
$$
\frac{4z^{513}}{c_-\,513(1-z)}<10^{-10}.
\tag{37}
$$

同次公开精确执行得到
$$
\boxed{
\begin{aligned}
\frac{4512687}{10^6}
 &<L'(E_{289},1)<\frac{282043}{62500},\\
\frac{251647}{50000}
 &<L'(E_{83521},1)<\frac{5032941}{10^6}.
\end{aligned}}
\tag{38}
$$
两曲线解析秩准确为一。
原有理点 $(-4,15)$、$(42,397)$ 均在相应曲线上，
且各 $y^2$ 不整除短 Weierstrass 判别式 $-432(17^k)^2$，
故 Lutz–Nagell 也直接证明它们非挠。
这些点及其更强的 End 独立性另由 R733 支付。

## 8. 真实共轭 Katz 值与一次 logarithm

### 8.1 所用原定理及本篇全部假设

本篇引用的是 BDP 2012 **已发表 Theorem 1，印刷第262页、式(1-1)**，
即文中明确标为 Rubin 1992 的共轭 Katz 定理；
不是把经典插值区内的一个恒等式延用到反象限。
本篇的逐项代入如下。

| 原定理的数据/假设 | 本篇实际数据与证明 |
| --- | --- |
| $A/\mathbf Q$，几何 CM 环为 $\mathcal O_K$ | $A=E_k:y^2=x^3+17^k$，$k=2,4$；$K=\mathbf Q(\sqrt{-3})$，$j=0$，全部 CM 在 K 定义 |
| 曲线自身的型 $(1,0)$ Hecke 角色 | 式(5)的 $\psi_k$；$\psi_k\bar\psi_k=\mathrm N$，中心角色为 $\epsilon_K\mathrm N$ |
| 好分裂 p | 原 ray 给 $p\equiv1\bmod3$；删原固定坏集后 $p>163$，特别 $p\nmid 2\cdot3\cdot17$ |
| 曲线 L 函数在1准确一阶零 | 本篇(7)、(36)–(38)：完整导子10404、root $-1$、严格 $L'(E_k,1)>0$ |
| 使用的 p-adic L 函数 | Theorem3.1、Proposition3.5 的同一 primitive Katz 函数，原导子 $(34\delta)$；三处原坏点均分歧 |
| 规范微分 | $\omega_{E_k}=dx/(2y)$，定义于 $\mathbf Q$；其普通周期在(40)与原 $\Omega_p$ 同步 |

若通过该文 Theorem2 的一般形式核对，附加条件(1-6)–(1-9)也全部成立：
$D=3$为奇数，$\mathfrak f=(34)\mathfrak d_K$且$\mathfrak d_K=(\delta)$恰一次，
$34$与3互素，值域 $E_{\psi_k}=K$，root为 $-1$。
曲线本身的导子含惰性素数2、17，
**本篇没有声称 $(\theta_{\psi_k},K)$ 满足 cyclic-ideal Heegner hypothesis**。
在 BDP 的证明中，需该假设的是 Definition3.19 的辅助 good pair；
其存在与补充 L 值非零由 Proposition3.28 支付，
Heegner 点经 Lemma3.25、Proposition3.27 回到原 CM 因子。
本篇直接使用最终 Theorem1，
不使用另加 $\mathcal O_K^\times=\{\pm1\}$ 的 §3G 特例 Theorem3.35。
因此 $K=\mathbf Q(\sqrt{-3})$ 的六个单位没有被漏掉。

Theorem1 给出一个实际
$\widetilde P_{k,p}\in E_k(\mathbf Q)$ 无限阶点及
$\widetilde\epsilon_{k,p}\in K^\times$，满足其式(1-1)。
这不是只在未识别的高维 CM variety 上得到一个点。
由解析秩一的 Gross–Zagier–Kolyvagin 定理，
$E_k(\mathbf Q)\otimes\mathbf Q$ 是一维；
BDP 印刷第263页步骤(2)和 Lemma3.25 的秩一论证也明确使用这一结论。
取 R733 的固定非挠点
$$
P_2=(-4,15),\qquad P_4=(42,397).
\tag{39a}
$$
于是存在 $r_{k,p}\in\mathbf Q^\times$，
使 $\widetilde P_{k,p}=r_{k,p}P_k$ 在
$E_k(\mathbf Q)\otimes\mathbf Q$ 中成立。
整数分母与挠点都被原形式群对数准确处理。
将 $r_{k,p}^2$ 吸收到
$\epsilon_{k,p}=\widetilde\epsilon_{k,p}r_{k,p}^2\in K^\times$，得到
$$
\mathcal L^{\rm prim}_{p,34\delta}(\bar\psi_k)
=\epsilon_{k,p}\,\Omega_{p,E_k}^{-1}
          \log_{\omega_{E_k}}(P_k)^2 .
\tag{39}
$$
保留定理的 $K^\times$ 歧义；不假设它与 p 无关或处处为单位。
这里已经把实际 Katz 点与 R733 的**同两个固定点**接齐。

### 8.2 共同周期、微分与代数线性独立

选择共同 CM periods
$$
\varpi_{E_k}=\theta^{-k}\varpi_0,\qquad
\Omega_{p,E_k}=\theta^{-k}\Omega_{p,0}.
\tag{40}
$$
这是实际微分拉回的代数尺度。
Katz 插值在复/普通周期同时乘这个代数因子时不变，
BDP Theorem 3.1 的原文亦明确说明这一点。
所以 (39) 与 (33) 使用同一个 Katz 函数。

无限阶有理点的 $p$-adic logarithm 非零：
先乘非零整数使点落进对数单射的形式群球，再用可加性。
因此 (39) 与 (34) 证明 (4) 非零。
相反，形式复等式
$L(\psi_k^{-1},0)=L(\bar\psi_k,1)=L(E_k,1)=0$
在此恰是解析秩一中央零，不能代替 (39)。
负点不在所选 Katz 经典插值象限，
其非零来自真正的共轭 Katz/Heegner 点定理。

为对接 R733，令 $t=\theta^2=\sqrt[3]{17}$，
取真正代数同构到 $E_1:y^2=x^3+1$：
$$
\phi_2(x,y)=(x/t^2,y/17),\qquad
\phi_4(x,y)=(x/t^4,y/289).
\tag{41}
$$
这里 $t^4=17t$。
有
$\phi_2^*\omega_1=t\omega_{E_2}$、
$\phi_4^*\omega_1=t^2\omega_{E_4}$，
所以
$\log_{\omega_1}(\phi_kP)=\theta^k\log_{\omega_{E_k}}(P)$。
将 (4)、(39)、(40) 合并：
$$
\boxed{
\Omega_p I_{k,p}
=A_{k,p}\log_{\omega_1}(\phi_kP_k),\qquad
A_{k,p}^{\,2}
=\frac{\epsilon_{k,p}\theta^{-k-12}}{34c_k}
 \in\overline{\mathbf Q}^{\,\times}.
}
\tag{42}
$$
平方根在原 $\mathbf C_p$ 中选择与实际等式相符的一支；
由于其平方是代数数，该支仍属于固定嵌入的
$\overline{\mathbf Q}^{\,\times}$。
(42) 是一次 logarithm 公式，不是把 $I_{k,p}$ 当作 logarithm 的平方。

R733 以两个不同三次 Galois 角色证明 (39a)、(41) 的两个固定非挠代数点
在 $\operatorname{End}_{\overline{\mathbf Q}}(E_1)$ 上独立，
再用 p-adic analytic subgroup theorem 得到其 logarithms
在 $\overline{\mathbf Q}$ 上线性独立。
这里 Galois 仅作用于代数点；没有假设它连续作用于整个 $\mathbf C_p$。
由共同周期 (42)，得到
$$
\boxed{
r_2 I_{2,p}+r_4 I_{4,p}\ne0
\quad\text{对任意 }(r_2,r_4)\in\overline{\mathbf Q}^{\,2}\setminus\{(0,0)\}.
}
\tag{43}
$$
系数可以随 p 及其他深度改变，只要每次确为代数数。
本篇不用“任意 $\mathcal O_p$ 单位”代替该假设。

## 9. 同一 R734 测试的深度量词与完整补偿

R734 的实际整逆给
$$
\mathcal D_{q_N^*}(0)=\frac{c}{a}D_{\omega,17}+\frac1aD_{-,17},
\qquad a,c\in K^\times .
$$
其 $\lambda=-\bar\pi_0^{-1}$、$\kappa=p\lambda^2$、$u=\kappa^N$
全在 K，混次测试的 $\Omega$ 已在完整来源坐标逐项消去。
因此 (43) 真正适用，得到原负一行
$$
\mathfrak I_N
=\Omega_p\left(\frac ca I_{2,p}+\frac1a I_{4,p}\right)\ne0
\quad\text{对所有合格 p、所有 }N\in4\mathbf Z_{>0}.
\tag{44}
$$

还可支付原偶步提取需要的赋值量词。
固定一个 R734 的合格 p。
a、c 是 u 的有理函数，按其已付单位分母在 $u=0$ 整解析，
且 $a(0),c(0)$ 仍为 K 中的单位。
故
$$
\mathfrak I_\infty
=\Omega_p\left(\frac{c(0)}{a(0)}I_{2,p}
                       +\frac1{a(0)}I_{4,p}\right)\ne0 .
$$
当 $N\to\infty$、$N\in4\mathbf Z$ 时，$\mathfrak I_N\to\mathfrak I_\infty$，
从而其赋值最终为同一个有限值 $v_p(\mathfrak I_\infty)$。
对充分大的这种 N，准确有
$$
v_p(\mathfrak I_N)<N .
\tag{45}
$$
这不声称有 p 一致的估值上界。

于是 R734(25) 的原偶步 $P_{31}$ 行在所有 $n>N$ 上严格满足
$$
\boxed{
v_p\!\left(\mathscr P_{31}^{(2)}
       (\mathcal I^T_{\rm pair})'(0)\right)
=N+v_p(\mathfrak I_\infty)<2N .
}
\tag{46}
$$
所有 $\lambda$、$U_{31}^{(2)}$、$b_Y$、$(p-1)$ 和 $\Omega_p$ 都是原单位；
$p^{2N}$ 高 k 尾不会抵消首项。
固定 p、N 后测试不依 n，所以有限偶步过滤合法。

与 (46) 同时成立的完整外部身份仍是
$$
\mathscr P_{31}^{(2)}(\mathcal O^T_{\rm pair})'(0)
=-\mathscr P_{31}^{(2)}(\mathcal I^T_{\rm pair})'(0).
\tag{47}
$$
故本文得到了同一实际算术测试下的严格非零内/外补偿。
(47) 不能被舍去，也不能把 (46) 直接认作原 $J'_T\ne0$。
原三条合格曲线的中央假设及主完成标准仍按原 README 保持。

## 10. 可重现执行、来源与范围

### 10.1 完整有限 Schwartz

脚本：
[check-r732-type-five-full-local-schwartz.py](../scripts/check-r732-type-five-full-local-schwartz.py)，无参数，
python-flint==0.9.0。它从 $\Phi_{51}$、$\Phi_{24}$ 和 (12) 重建，
不读取旧数据，不保存生成输出。

- source commit：112af4c4f7d0de0009ae673115b8ca142364de89。
- public run：43703192796；job：132778575004。
- script SHA256：7ebdd96f29d5a6e0027b9de913dd596a055700511ba284005c3c7467fa5d6046。
- stdout：2775字节；SHA256：
  04a5b3c7f6125f60081be87f1eed437ba3fc327b77617b941031d1fa1f9924dd。
- 实际完成全部28项准确断言。

### 10.2 严格解析秩一

脚本：
[check-r732-two-cubic-rank-one-bounds.py](../scripts/check-r732-two-cubic-rank-one-bounds.py)。
命令：python check-r732-two-cubic-rank-one-bounds.py --cutoff=512 --series-terms=144。

- source commit：66e8cf02a0e31459fb9b3b50099cbc807c40d177。
- public run：43701949704；job：132774806522。
- script SHA256：abc12f49db1818351534889f31bd9b7bac7876a78cbd043a060834d97c2a8289。
- stdout：654字节；SHA256：
  318033986371d91ac19c1a6f2977e8f277e5e0eabf9fbed6b976e8f2f1753608。

所有区间和原 Fourier 系数由脚本重算，不提交生成输出。

### 10.3 文献及已付原接口

- R290、R292、R306：同一实际 Yang 极化、标准半周期下降、完整2/3/17模型、类数与体积；本篇保新二处线和新奇三次向量。
- R732：全十三纤维的特征零算子、两条单重型五来源及不可约三维余块。
- [R733](R733-two-cubic-points-and-algebraic-independence-of-p-adic-logarithms.md)：两个原曲线点在同一 $E_1$ 上的 End 独立及 p-adic analytic subgroup theorem；只用于 (43) 以后。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：实际五维整逆、全原来源/域、真实代数系数及相反外部。
- J. H. Silverman–K. E. Stange, *Amicable Pairs and Aliquot Cycles for Elliptic Curves*,
  §6、Theorem 19 证明中的完整六次公式：
  <https://arxiv.org/pdf/0912.1831>。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math. 485 (1997),
  Theorem 1.11、Corollary 2.14、Theorems 2.6、2.15：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*,
  Compositio Math. 117 (1999)，§1、Appendix(A1)–(A11)：
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- M. Bertolini–H. Darmon–K. Prasanna, *p-adic Rankin L-series and rational points on CM elliptic curves*,
  Pacific J. Math.260 (2012), Theorem1、Proposition2.11、Theorem2.12、
  Theorem3.1、Proposition3.5：
  <https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf>。
  primitive插值及同步周期不变性分别见(3-1)、其后说明；
  共轭 Katz 负点的真非零来自 Theorem1，不由普通插值或裸 functional equation 推得。
