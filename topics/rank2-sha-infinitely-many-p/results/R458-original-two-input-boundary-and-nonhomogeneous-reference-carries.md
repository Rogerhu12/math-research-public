# R458 — 原两输入补域、完整六行与参考相消支的非齐次差

日期：2026-11-14。**状态：已证明。**

本篇保留 R455 的原独立 sigma 输入 \(c\) 及真实 \(Z\) 边际，
将剩余外域准确分成两个一单位支和一个双单位不相消支。
两条不同方向的近相消支完整返回同一组六条固定完整来源；
原 \(Z,c\) 核心的符号不同，全部保留。

按物理 \(p^r\) 归一第一输出时，实际质量产生
\(r(p-1)\log(\kappa/p)\) 项。对两条已识别的秩零参考，
两个实际相消支之间的差严格消去未知参考导数，留下已知非零
对数项；原 \(S\) 的对应项因质量零消失。另一个原输入支
\(c\) 深、\(Z\) 单位的中央首阶是一，不能被原 \(Z\) 深支
的第五阶取代。本文保留全部双单位补偿；主目标尚未完成。

## 1. 同一个完整来源及两个原输入

保持 R454、R455 的原 \(b=17\)、周期 \(\Omega\)、固定普通 ray
以及
\[
\lambda=-\bar\pi_0^{-1},\quad \kappa=p/\bar\pi_0^2,\quad
\chi=\chi_{33,p}\in\{1,-1\},\quad d=p-1.
\tag{1}
\]
仍有 \(p\equiv7\pmod {64}\)、\(p\ge71\)。记
\[
H_{33}=S/\sigma,\qquad
\nu_H=\nu_{-2H_{33}/3},\qquad
\rho=\nu_\sigma(c)\otimes\nu_H(Z).
\tag{2}
\]
这是 R455 的完整真实边际，不是另选的抽象乘积。
原三输入 \(\Phi_+\) 的输出 \(T=Z-33H\) 有完整标量核心
\(\beta_T=-\eta\chi\lambda\)，保持整个 \(Z,c\)。
因此本篇只依赖 \(Z,c\) 的任一域和测试，若再附 \(T\in p^n\)，
整条结果准确乘 \(\beta_T^n\)。这里使用完整核心，不从边际
倒推未保留的条件。

使用
\[
Y=Z+c,\quad T_c=Z-33c,\qquad
Z=(33Y+T_c)/34,\quad c=(Y-T_c)/34.
\tag{3}
\]
原生成函数是已付的整个无 twist 来源
\[
F(y,t)=-\frac23\sigma(y-33t)H_{33}(y+t)
\in\mathcal S_{34}\boxtimes\mathcal S_{1122}.
\tag{4}
\]
写
\[
s=-\lambda,\qquad a=\chi\lambda,\qquad q=-\chi\lambda.
\tag{5}
\]
两个原输入和两个完整输出的核心为
\[
\begin{aligned}
\nu_\sigma|_{p\mathbf Z_p}&=s[\kappa]_*\nu_\sigma,&
\nu_H|_{p\mathbf Z_p}&=a[\kappa]_*\nu_H,\\
K_YF&=R_YF,&K_{T_c}F&=-\chi R_YF.
\end{aligned}
\tag{6}
\]
特别同时原输入深的系数是
\[
\boxed{sa=-\chi\lambda^2=\lambda q.}
\tag{7}
\]
原 sigma 的 \(s=-\lambda\) 不能换成 \(+\lambda\)。

## 2. 六条完整来源行及全部质量

对 \(1\le k\le6\)，令 \(m_k=6k\)，并记
\[
F_k(y)=m_k![t^{m_k}]F(y,t),\qquad
\Gamma_k(u)=\int_{Y\ {\rm unit}}\langle Y\rangle^{du}
                     (T_c/\Omega)^{m_k}\,d\rho.
\tag{8}
\]
R455 已在整个六维型零格中证明
\[
F_k(y)=\sigma_b(y)^{34}\sum_{j=0}^5
          M_{jk}b^{k+4-j}x_b(y)^{2+3j}.
\tag{9}
\]
这里 \(M_+=(M_{jk})_{0\le j\le5,1\le k\le6}\) 是该篇由
Weierstrass 递推重建的完整可逆有理矩阵。\(\Gamma_k\) 是
\(\nu_{F_k}\) 的整条 principal 函数，不只是一个中央数。

每条 \(F_k\) 的第一型为零，反射在其上为一。令
\[
\mu_k=\Gamma_k(0),\qquad
E_k=1-q\kappa^{m_k}=1+\chi\lambda\kappa^{6k}.
\tag{10}
\]
完整质量为
\[
\boxed{\mu_k=(1-\lambda)M_{5k}b^{k-1},}
\tag{11}
\]
其中最后一行准确是
\[
\begin{aligned}
(M_{51},\ldots,M_{56})={}&(
15840,\ 64807209920471040,\
-130392183831881710111990087680,\\
&-1844290970369941856587730293056075139645440,\\
&6465891770686273552780094894218131326687914758242304000,\\
&-279995506460853511232612089925237737507091779662380286533416098201600).
\end{aligned}
\tag{12}
\]
来源质量是 \(F_k(0)\)；限制第一单位域后才乘 \(1-\lambda\)。
Tc 深域贡献为 \(q\kappa^{m_k}\Gamma_k\)，故完整有
\[
\boxed{\int_{Y,T_c\ {\rm unit}}\langle Y\rangle^{du}
              (T_c/\Omega)^{m_k}\,d\rho=E_k\Gamma_k(u).}
\tag{13}
\]
这保留全部质量；所有 \(E_k\) 均是单位。

## 3. 两个一单位支与唯一双单位主块

对 \(t\in p\mathcal O\)，在同一原输入上定义
\[
\begin{aligned}
A_k(t,u)&=\int_{c\ {\rm unit}}\int
 \langle c+tZ\rangle^{du}
 ((tZ-33c)/\Omega)^{m_k}\,d\nu_H(Z)d\nu_\sigma(c),\\
B_k(t,u)&=\int_{Z\ {\rm unit}}\int
 \langle Z+tc\rangle^{du}
 ((Z-33tc)/\Omega)^{m_k}\,d\nu_\sigma(c)d\nu_H(Z).
\end{aligned}
\tag{14}
\]
主单位条件由未缩放输入给出，对数展开合法。令
\[
\mathscr C=\{c,Z,Y,T_c\ {\rm unit}\},\qquad
C_k(u)=\int_{\mathscr C}\langle Y\rangle^{du}
                          (T_c/\Omega)^{m_k}\,d\rho.
\tag{15}
\]
因 \(34\) 是单位，准确不交分拆为
\[
\{Y,T_c\ {\rm unit}\}
=\{Z\in p,c\ {\rm unit}\}\sqcup
 \{c\in p,Z\ {\rm unit}\}\sqcup\mathscr C.
\tag{16}
\]
于是六条完整方程是
\[
\boxed{E_k\Gamma_k(u)
=aA_k(\kappa,u)+sB_k(\kappa,u)+C_k(u),\quad1\le k\le6.}
\tag{17}
\]
对 \(n\ge1\)，两个更深的实际输入支分别是
\[
\boxed{a^nA_k(\kappa^n,u),\qquad s^nB_k(\kappa^n,u).}
\tag{18}
\]
这里始终保原 \(Z,c\)，没有从总输出深度倒推独立输入深度。

全部质量是有限代数矩。写完整矩为
\(\mu_j^\sigma,\mu_j^H\)，单位矩为 \(I_j^\sigma,I_j^H\)，则
\[
\begin{aligned}
A_k(t,0)&=\Omega^{-m_k}\sum_{j=0}^{m_k}
 \binom{m_k}{j}t^j(-33)^{m_k-j}\mu_j^H I_{m_k-j}^\sigma,\\
B_k(t,0)&=\Omega^{-m_k}\sum_{j=0}^{m_k}
 \binom{m_k}{j}(-33t)^j\mu_j^\sigma I_{m_k-j}^H,\\
C_k(0)&=E_k\mu_k-aA_k(\kappa,0)-sB_k(\kappa,0),\\
I_j^\sigma&=(1-s\kappa^j)\mu_j^\sigma,\qquad
I_j^H=(1-a\kappa^j)\mu_j^H .
\end{aligned}
\tag{19}
\]
\(C_k'(0)\) 仍是实际未知中央。式 (17) 将它保在原六条来源行
和两个明确输入支中，没有因其为补域而赋零。

## 4. 两条近相消支的完整返回

两个相消斜率 \(Z/c=-1,33\) 模当前 \(p\) 不同。对 \(r\ge1\)，令
\[
\begin{aligned}
\mathscr N_{Y,r}
 &=\{c,Z\ {\rm unit},Y\in\kappa^r\mathbf Z_p^\times\},\\
\mathscr N_{T,r}
 &=\{Y\ {\rm unit},T_c\in\kappa^r\mathbf Z_p^\times\}.
\end{aligned}
\tag{20}
\]
第一域自动有 \(T_c\) 单位，第二域自动有 \(c,Z\) 单位。
只在这些域中作显示的整归一，定义
\[
\begin{aligned}
N_{Y,r,k}^{\kappa}(u)&=\int_{\mathscr N_{Y,r}}
 \langle Y/\kappa^r\rangle^{du}(T_c/\Omega)^{m_k}\,d\rho,\\
N_{T,r,k}^{\kappa}(u)&=\int_{\mathscr N_{T,r}}
 \langle Y\rangle^{du}(T_c/(\kappa^r\Omega))^{m_k}\,d\rho.
\end{aligned}
\tag{21}
\]
准确有
\[
\boxed{
N_{Y,r,k}^{\kappa}(u)=\lambda^rE_k\Gamma_k(u),\qquad
N_{T,r,k}^{\kappa}(u)=q^rE_k\Gamma_k(u).}
\tag{22}
\]

第一式必须减去两个原输入同时深的行。所有
\(Y\in\kappa^r\mathbf Z_p^\times\) 给 \(\lambda^r\Gamma_k\)；
其中 \(c,Z\in p\) 由 (7) 和上一层第一环带给
\[
sa\,\kappa^{m_k}\lambda^{r-1}\Gamma_k
=q\lambda^r\kappa^{m_k}\Gamma_k.
\]
相减就是第一式。第一输出的反射由 principal 测试准确消去。
第二式则先用完整 Tc 深核心，再限制归一 Tc 为单位；
该单位行正是 (13)。若不归一 Tc，第二式必须再乘
\(\kappa^{rm_k}\)。

Tc 方向的正次数允许收敛求和：
\[
\sum_{r\ge1}(q\kappa^{m_k})^rE_k\Gamma_k
=q\kappa^{m_k}\Gamma_k.
\tag{23}
\]
这只重建完整 Tc 深域。Y 方向的 \(\lambda^r\) 是单位，
不能依同样理由删去无限深余域，也不能将该方向未付的无限和
当作已存在的积分。

## 5. 物理 \(p^r\) 归一产生的真实质量项

令
\[
\xi=\kappa/p=\bar\pi_0^{-2}=\lambda^2,\qquad
\ell=d\log_p\langle\xi\rangle.
\tag{24}
\]
将 (21) 第一行改用 \(Y/p^r\)，记为 \(N_{Y,r,k}^{p}\)。
两测试准确相差单位 \(\xi^r\)，所以
\[
\boxed{
N_{Y,r,k}^{p}(u)=
\lambda^rE_k\langle\xi\rangle^{rdu}\Gamma_k(u).}
\tag{25}
\]
中央及质量为
\[
\boxed{
(N_{Y,r,k}^{p})'(0)
=\lambda^rE_k\{\Gamma_k'(0)+r\ell\mu_k\},\qquad
N_{Y,r,k}^{p}(0)=\lambda^rE_k\mu_k.}
\tag{26}
\]
于是同一两方向的实际环带满足
\[
\boxed{
\lambda^{-r}(N_{Y,r,k}^{p})'(0)
-q^{-r}(N_{T,r,k}^{\kappa})'(0)
=r\ell E_k\mu_k.}
\tag{27}
\]
这里的质量是 (11)，不是抽象待定常数。
若用自然非零 \(Y\) 的 \(\log_pY\)，同一项写为
\(r\,d\log_p\kappa\)；因 \(\log_pp=0\)，它等于 \(r\ell\)。

还有 \(\ell\ne0\)：当前分裂处 \(\xi\in\mathbf Z_p^\times\)，
\(p>2\) 时此群上的 log 核为根单位；但
\(\xi=\bar\pi_0^{-2}\) 的代数范数是 \(p^{-2}\)，不可能是根单位。
这不使用参考中央导数，也不预付 \(\ell/p\) 是单位。

## 6. 在同一六列中抽出原参考，并消去其未知导数

保留 R307、R447 原参考 \(H_3,H_5\)，质量均为一。在 (9) 的
固定系数格中，令
\[
\begin{aligned}
\mathbf s&=(-128/7,-80/7,-12/7,-53/7,1,0)^{\mathsf t},\\
\mathbf r_3&=(-2048,12032,8128,400,-208,1)^{\mathsf t},\\
\mathbf r_5&=(1024,-6784,-14912,-272,272,1)^{\mathsf t},\\
\mathbf c&=M_+^{-1}\mathbf s,\qquad
\mathbf d_a=M_+^{-1}\mathbf r_a\quad(a=3,5).
\end{aligned}
\tag{28}
\]
这是完整确定的有限有理定义。六项系数全附于 JSON，
而 (28) 及 R455 的完整矩阵也独立准确确定每个数。
定义
\[
\begin{aligned}
h_S^\times(t)&=\sum_{k=1}^6
              c_kb^{-k}t^{6k}/E_k,\\
h_a^\times(t)&=\sum_{k=1}^6
              d_{a,k}b^{1-k}t^{6k}/E_k\quad(a=3,5).
\end{aligned}
\tag{29}
\]
第一条正是 R455 的原测试；另外两条仍只用相同六个正 Tc 次数。
只需固定排除这些有理系数分母的素因子，没有随 \(p\) 增长的次数。

由 (9)、(13)，三条 Tc 单位行分别完整抽回
\[
J_S(u),\qquad J_{H_3}(u),\qquad J_{H_5}(u),
\tag{30}
\]
其质量分别为 \(0,1-\lambda,1-\lambda\)。按同一 (29) 组合
两种实际环带，得到
\[
\boxed{
N_{Y,r,G}^{p}(u)=\lambda^r\langle\xi\rangle^{rdu}J_G(u),\qquad
N_{T,r,G}^{\kappa}(u)=q^rJ_G(u),\quad G=S,H_3,H_5.}
\tag{31}
\]
第二行使用的是真测试
\(h_G^\times(T_c/(\kappa^r\Omega))\)，不是未归一旧测试。

对每条原参考，准确非齐次关系为
\[
\boxed{
\lambda^{-r}(N_{Y,r,H_a}^{p})'(0)
-q^{-r}(N_{T,r,H_a}^{\kappa})'(0)
=r\ell(1-\lambda),\quad a=3,5.}
\tag{32}
\]
它消去两域中同一个未知 \(J'_{H_a}(0)\)；右侧对每个
正整数 \(r\) 都非零，但没有声称赋值固定为一。
只用两个相邻 Y 环带也有
\[
\boxed{
\lambda^{-r-1}(N_{Y,r+1,H_a}^{p})'(0)
-\lambda^{-r}(N_{Y,r,H_a}^{p})'(0)
=\ell(1-\lambda).}
\tag{33}
\]
这些是同一个原联合的实际测试，不是根据质量猜导数。
对 \(S\)，两个右侧准确为零。因此尚需真正改变第一输出的
算术来源关系，把参考非齐次差接到原 \(S\) 行；六维可逆
线性重写本身不提供这条关系。

## 7. 原 \(c\) 深支的一阶首项，保全部 log 项

先用 R455 固定未调整测试
\(h_b(t)=\sum_{k=1}^6c_kb^{-k}t^{6k}\)，把 (14) 的 \(B\) 按其
组合并在 \(u=0\) 求导，记为 \(\mathcal B(t)\)。完整展开给
\[
\boxed{
[t]\mathcal B
=d\sum_{k=1}^6c_kb^{-k}\Omega^{1-6k}
 \{I^H_{6k-1}-198k I^H_{6k-1,\log}\}.}
\tag{34}
\]
其中
\(I^H_{m,\log}=\int_{Z\ {\rm unit}}Z^m
\log_p\langle Z\rangle\,d\nu_H\)。
第二项来自整个多项式的一阶变化，不能作为“常数 log”删去。

写 R455 的准确级数为
\[
\sigma(z)=z\sum_{j\ge0}a_jb^jz^{6j},\qquad
H_{33}(z)=z^5\sum_{j\ge0}r_jb^jz^{6j},\quad r_0=1.
\tag{35}
\]
那么
\[
\mu_{6k-1}^H=-\tfrac23(6k-1)!r_{k-1}
                      b^{k-1}\Omega^{6k-1},\qquad
I_m^H=(1-a\kappa^m)\mu_m^H.
\tag{36}
\]
所有 \(I^H_{m,\log}\in p\mathcal O\)，所以
\[
[t]\mathcal B\equiv(d/b)\beta\pmod p,
\]
\[
\boxed{
\begin{aligned}
\beta&=-\tfrac23\sum_{k=1}^6c_k(6k-1)!r_{k-1}\\
&=-\frac{7739405069281599646676344610350618630990965049318085}
{263148240146991169523590689745234989500086260569006478606336}
\ne0.
\end{aligned}}
\tag{37}
\]
这是固定特征零运算，不是目标素数扫描。

原 sigma 只有 \(1\bmod6\) 次矩，故此前无常数项。
固定三十六次测试及完整 log 展开给
\[
v_p([t^j]\mathcal B)\ge-\lfloor\log_pj\rfloor.
\tag{38}
\]
去掉显示常数的分子分母素因子后，首项为单位，并对每个
\(n\ge1\) 严格支配所有高尾。因此
\[
\boxed{
v_p\!\left(\int_{c\in p^n,Z\ {\rm unit}}
d\log_p\langle Y\rangle\,h_b(T_c/\Omega)\,d\rho\right)=n.}
\tag{39}
\]
换成同一实际 \(h_S^\times\) 后六个系数只改 \(p^6\) 倍，
首项不变；若再附原 \(T\in p^n\)，值乘单位 \(\beta_T^n\)，
赋值仍为 \(n\)。这与 R455 的 \(Z\) 深支赋值 \(5n\) 是两个
不同的原输入域。

## 8. 双单位主块的实际质量和中央补偿

同一 \(B\) 支的质量首项也能完整算出。把 (19) 按 \(h_b\)
组合，记为 \(\mathcal B_0(t)\)，则
\[
[t]\mathcal B_0\equiv\delta/b\pmod p,
\]
\[
\boxed{
\begin{aligned}
\delta&=22\sum_{k=1}^6(6k)c_k(6k-1)!r_{k-1}\\
&=\frac{73597540986890629732530587670468324477591396942553901805}
{12638425200392992558508008404708647134601365125661450041954304}
\ne0.
\end{aligned}}
\tag{40}
\]
这是多项式测试的真实质量，不是中央导数。

令 \(C_S^\times(u)\) 是 \(\mathscr C\) 上用实际 \(h_S^\times\)
的行。由 (17)、R455 第五阶及 (34)–(40)，准确有
\[
\boxed{
\begin{aligned}
C_S^\times(0)&\equiv\lambda\kappa\,\delta/b\pmod {p^2},\\
(C_S^\times)'(0)&\equiv
J'_S(0)+\lambda\kappa\,d\beta/b\pmod {p^2}.
\end{aligned}}
\tag{41}
\]
第一行只用已知 \(J_S(0)=0\)。Euler 调整系数差在 \(p^6\)，
不会改变这两项。固定有限坏集可统一取为下列数的素因子：
R455 已显示的坏整数、\(\beta,\delta\) 分子分母，以及
(28) 三个固定向量的共同分母。完整脚本输出一个显示整数
作为公倍数，不假定其素因子分解。

删去该固定有限集后，(41) 第一行质量赋值恰为一；
若另假设 \(J'_S(0)=0\)，第二行准确给
\[
\boxed{v_p((C_S^\times)'(0))=1.}
\tag{42}
\]
原中央零并不令此主块变零，而是要求一个真实的一阶补偿。
它不能被原第五阶管单独排除。

## 9. 已付接口与仍需解决的来源关系

原六条来源行、两个输入深支、两条近相消支、双单位主块及
全部质量已经在 (17)、(22)、(26) 中对齐。
参考的未知导数在 (32)、(33) 中由两个真实域严格消去，
留下非零的已知代数单位对数。

剩余任务是用真正改变 \(Y\) 的算术来源关系把这个非齐次差
接到原 \(S\) 的零行，或直接控制 (17) 的双单位主块。
只有保 \(Y\) 的新核心、或对六条行再作可逆组合，不会自动
提供该关系。所有附加 \(T\) 条件由完整核心支付；
所有 \(\kappa^{-r}\) 只在准确像域使用；没有向内部域免费
分配完整中央零。

## 精确文件与依赖

- [完整精确脚本](../scripts/check-r458-original-two-input-boundaries.py)
  使用 R455 已重建的全来源矩阵，核对三条实际来源、全部质量、
  两原输入相位、两个一阶系数及非齐次 carry 代数。
- [完整有理数据](../scripts/check-r458-original-two-input-boundaries.json)
  给两参考全部六项系数、质量行、log 碰撞系数及固定坏整数。
- [R455：同一纯 Tc 来源、六列及原非零管](R455-original-pure-companion-test-and-slope-core-arithmetic-return.md)。
- [R454：奇 degree33 核心与保原输入的斜轴](R454-original-odd33-core-and-exact-residual-slope-transport.md)。
- [R447：两个原参考及完整共同规范](R447-original-two-reference-intersection-and-fixed-degree18-tests.md)。

