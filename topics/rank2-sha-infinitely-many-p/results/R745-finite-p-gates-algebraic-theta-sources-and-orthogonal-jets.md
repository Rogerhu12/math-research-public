# R745 — 原有限 p 门的代数 theta 来源与正交正矩收缩

日期：2026-11-15。**状态：下述有限化及代数系数结论已证明。**

本篇支付 R737/R740 点公式接口之前的一项来源问题：
保完整有限 p 门后，可以先用有限 Fourier 展开，再收缩全部正交伙伴的有限正矩。
得到的是有限个有代数系数的真正 theta 截面及其原 torsion 平移，
而不是任意未知的 \(\mathbf C_p\) 条件系数。

积分中的单位负一算子仍完整保留。
本篇没有把这些全部截面缩成 R735 的两条线，也没有证明其负一值已经是代数点 logarithm。
对有理返回轴，清分母的真实 degree/level 成本一并保留，不能免费称仍是一个裸 34 维来源。

## 1. 原物理行与生成列的约定

固定原普通素数 p、同一个 K 嵌入及原周期 \(\Omega=\Omega_p\)。
使用 E17 的代数微分 \(dx/(2y)\)。
六个物理测度变量按
\((\xi_1,\xi_2,\xi_3,x,c,d)\) 排列。
原 Y 行为
\[
y=(\delta,2\delta,\gamma_7,\bar\gamma_7,1,2),
\qquad Y=y\xi,\qquad N(y)=34 .
\tag{1}
\]
物理投影的对偶列是 \(\bar y^{\,t}/34\)。
但 Amice/生成变量与 \(\xi\) 作**双线性**配对，所以生成嵌入准确为
\[
\iota_Y(z)=y^t z,
\tag{2}
\]
不是 \(\bar y^t z\)。
若 \(r\) 是原物理伙伴行，则其生成方向同样为 \(r^t w\)。

原完整伙伴可取
\[
r_1=17Z,\quad r_2=E,\quad r_3=R_2,\quad r_4=R_3,\quad r_5=R_4.
\]
R686/R740 的准确 Gram 给
\[
\operatorname{Gram}(y,r_1,r_2,r_3,r_4,r_5)
=\operatorname{diag}(34,8942,7627,5,330,638).
\tag{3}
\]
因此伙伴都与 Y Hermitian 正交；它们连同 y 给一个满秩代数 isogeny。
所有固定分母按原规范保留。
本篇只需要有理 isogeny 和代数性，不把 (3) 的十七因子视为单位。

将单个原 sigma 的 Amice 规范写成
\[
\widehat\nu_\sigma(T)=\sigma_{17}(\Omega\log(1+T))
\tag{4}
\]
时，等式首先是原点附近的形式复合。
原六输入 \(\mu_0\) 还含原 C 角平均；该平均是有限的，
其每个有理 CM 变换均固定 Y 并保同一正交补。
下面逐项对六 sigma tensor 证明，再对这个完整平均求和。
第二、第三态的全部 W-quarter lift 也逐项保留。

## 2. 每个原有限门的准确 Fourier 形式

令 \(C:\mathbf Z_p^6\to\overline{\mathbf Q}\) 为模 \(p^m\) 的局部常值函数。
选一个原始 \(p^m\) 次根 \(\zeta_m\)。
准确地
\[
C(\xi)=
 \sum_{a\in(\mathbf Z/p^m\mathbf Z)^6}
 c_a\,\zeta_m^{\,a\cdot\xi},
\qquad
c_a=p^{-6m}\sum_{v\bmod p^m}C(v)\zeta_m^{-a\cdot v}.
\tag{5}
\]
所有 \(c_a\) 都是代数数。
这是完整的六变量展开，不把混合 Y/Z/E 门改成互相独立的边际门。
门的值可以是 \(0,\pm1\)，也可以是已付的代数系数。

对任意原有界测度 \(\mu\)，乘上 (5) 的一个角色的真实 Amice 作用是
\[
\widehat{\zeta_m^{\,a\cdot\xi}\mu}(T_1,\ldots,T_6)
=
\widehat\mu\bigl(\zeta_m^{a_1}(1+T_1)-1,\ldots,
                \zeta_m^{a_6}(1+T_6)-1\bigr).
\tag{6}
\]
这来自有界测度定义，不需要对解析 logarithm 作非法代入。

特别不能把 \(\log_p\zeta_m=0\) 代进 (4)，
从而误认 (6) 为原来的 theta 函数。
原点附近的复合与 torsion 处的 p 进平移须由实际 theta 平移定理接合。

## 3. (6) 的代数 Mumford 平移及全部中心相位

这里使用 Bannai–Kobayashi 的明确比较，按 arXiv v4 的编号：
Theorem 2.9 给 torsion 的 Mumford 平移之代数 Taylor 系数；
Proposition 2.19 给 ordinary formal p-power 平移与该代数平移的精确比较。

具体地，先处理一个原 prime-to-p torsion 基点 \(v_0\)
（包括 quarter 来源已有的真实 lift），设其阶整除 \(N_0\)，且 \(p\nmid N_0\)。
令原 formal \(p^m\)-torsion 点对应周期类 \(v_m\)。
按固定 ordinary CM 型取 \(\epsilon\in\mathcal O_K\)，满足
\[
\epsilon\equiv1\pmod{\mathfrak p^m},\qquad
\epsilon\equiv0\pmod{2\bar{\mathfrak p}^{\,m}},\qquad
\epsilon\equiv2\pmod{4N_0}.
\tag{7}
\]
这些条件相容，由原普通分裂和 \(p\nmid2N_0\) 的 CRT 给出。
取实际半提升 \(v_0'=v_0/2\)；
它仍是 prime-to-p torsion，且
\(\epsilon v_0'=v_0+2\Lambda\)。
保相应 Mumford 周期因子
\[
\vartheta^M_{\epsilon v_0'}=c_0\,\vartheta^M_{v_0}.
\]
由原平移法则，\(c_0\) 是确定的代数根单位，不能免费置1。
Prop.2.19 的第一式准确给
\[
\widehat\vartheta^M_{v_0}(t\oplus t_{p^m})
=c_0^{-1}
 \langle\epsilon v_m,\epsilon v_0'/2\rangle_{\mathcal L}\,
 \widehat\vartheta^M_{\epsilon v_0'+\epsilon v_m}(t).
\tag{8}
\]
右侧配对和 \(c_0\) 均作为原中心因子保留。

这也处理原四挠基点：
不能同时要求 \(\epsilon\equiv0\bmod2\) 和
\(\epsilon\equiv1\bmod4\)。
对阶为奇数的基点，可以另取
\(\epsilon\equiv1\bmod N_0\)，使用该文式(32)的直接版本；
对完整 quarter 来源，本篇统一使用没有这个冲突的 (7)–(8)。
周期代表改变时，配对与 theta lift 同步改变，整个乘积不变。

(8) 逐个坐标应用到六 sigma；
随后保留原 C 平均、各 quarter 系数及所有中央 lift，得到 (6) 的准确代数 theta 描述。
对单 sigma，也可以直接使用该文 Theorem 2.12：
其规范 torsion 平移是带完整 quasi-period 指数补偿的 sigma，
而非一个未归一的裸 \(\sigma(z+v_0)\)。

本题 CM 格的六次对称使标准 sigma 与相应 reduced theta 的
二次指数差为零；或可一直使用 Theorem 2.12 的 sigma 规范。
因此没有新增一个待猜的非代数 Gaussian 常数。
原 sigma 的首项规范、原 algebraic differential 与 (8) 合起来，
使所需有限阶 Taylor 系数属于一个有限代数数域。
可以取含原 torsion 及适当 \(4N^2\)-torsion 的域；
不声称这个域在二或十七处不分歧，也不把它当成后续 Heegner 点的定义域。

若来源包含原有理 CM 变换，先清除其有限分母成为代数 isogeny；
选相容 torsion 提升后仍由 (8) 逐项给同一结论。
这只引入明确的有限 isogeny/torsion 层，不产生一般 p 进系数。
本篇不据该清分母操作删掉任何原有限相位。

## 4. 为什么正交伙伴的 jets 仍给真正的一变量 theta 截面

设 \(\mathcal L\) 是六 sigma 对应的 product line bundle，
先在 \(A=E_{17}^6\) 上处理一个原 tensor 项。
令 B 为 Y 的连通 Hermitian 正交补，
并考虑加法 isogeny
\[
s:E_{17}\times B\longrightarrow A,\qquad
s(z,w)=\iota_Y(z)+j(w).
\tag{9}
\]
正交性说对应 polarization 的交叉同态为零。
以原 rigidification 保留标量和半特征后，
\[
s^*\mathcal L\simeq
 \mathcal L_Y\boxtimes\mathcal L_B .
\tag{10}
\]
这个分裂在代数范畴中成立。
也可在 Appell–Humbert 数据中直接验证：
Hermitian 交叉项为零，semicharacter 的交叉配对同时为1。
不是仅在 Taylor 首项中省掉交叉项。

原 \(y\) 的各系数为整 CM endomorphism，故
\(\deg\mathcal L_Y=\sum N(y_i)=34\)。
对本题 (1)，各奇度 kernel 的点和为零，
两个偶度项 \(2\delta,2\) 各含完整的 \(E[2]\)，其 kernel 点和也为零。
因而未平移的准确 Y line bundle 是
\[
\mathcal L_Y\simeq\mathcal O_{E_{17}}(34[0]).
\tag{11}
\]
不存在一个漏记的二挠 flat twist。

对 (8) 所给的 torsion 平移，(10) 的两因子分别带真实 flat twist。
它们仍为外张量积；平移后的所有中心因子沿用 (8)。
沿 B 方向取任意有限正矩 jet，再令 B 变量为零，
只改变 \(\mathcal L_B\) 的有限 Taylor 系数，
不会改变 Y 的 automorphy factor。
所以每个 jet 是同一平移后的 degree34 line bundle 的 holomorphic section。

这种论证也覆盖来源中固定 Y 的有理 CM 变换：
它只重新选择 B 上的有限 isogeny 和代数微分方向，
Y 的 line bundle 和 (10) 的无交叉性不变。
原完整 C 平均须逐项相加，不能只认作一个边际标量。

为具体显示有限性，未平移的全空间有以下34个代数规范基：
\[
\sigma_{17}^{34}x_{17}^j\ (0\le j\le17),\qquad
\sigma_{17}^{34}y_{17}x_{17}^j\ (0\le j\le15).
\tag{12}
\]
这里极帽分别为 \(2j\le34\)、\(3+2j\le34\)。
平移后使用相应 Mumford-translated basis，完整保 flat character。

由 §3，伙伴 jet 的全部有限 Taylor 系数是代数数。
相应 basis 也可按同一个代数 rigidification 规范。
取足以区分这有限维空间的有限个 Taylor 系数，解实际线性系统，
即得该 jet 在 basis 中的系数全为代数数。
存在这样的有限系数集是因为一个非零 degree34 section
不可能在一点有大于34的零阶。
这一步仅证明有限代数展开，不作任何数值运行或抽样判断。

## 5. 原周期归一在全部混次块上逐项相消

设 \(P\) 是物理伙伴行上的齐次多项式，次数 D。
写生成函数的正交坐标为
\[
z_{\rm full}=y^t z+\sum_j r_j^t w_j .
\]
从原 Amice 定义和双线性配对，准确有
\[
\Omega^{-D}
 \int e^{Yz/\Omega}P(r_1\xi,\ldots,r_5\xi)\,
             C(\xi)\,d\mu(\xi)
=
\left.P(\partial_w)\Theta_C(y^t z+\textstyle\sum r_j^t w_j)
\right|_{w=0}.
\tag{13}
\]
\(\Theta_C\) 表示 (5)–(8) 后的完整有限 theta 组合。
(13) 中每一次物理矩产生恰一个 \(\Omega\)，
由显示的 \(\Omega^{-D}\) 逐项抵消。
所有 b 的齐次幂都是固定代数数。

原 R734/R737 的 \(\Phi_N\) 正是这种有限混次和：
每个齐次块按它自己的 \(b^{D/6}\Omega^D\) 归一，
实际整逆系数在 \(K(\lambda,\kappa,u)\)，
固定 p、N 后属于 K。
C-unit 等有限门由 (5) 处理；
原 E-test 的已付单位逆和两个完整 C 返回支仍逐项保留。
不能把所有次数统一除以一次 \(b\Omega^6\)。

对分子另含一条正交线性行 Z 的实际负一观察，
定义
\[
\nu_{N,C}
=\Omega^{-1}Y_*(Z\Phi_N C\,\mu).
\tag{14}
\]
由 (13)，其生成函数是 §4 所述的有限代数 theta 组合。
未留一般 \(\mathbf C_p\) 的伙伴系数。
准确的原积分则为
\[
\boxed{\quad
\int_{Y\ {\rm unit}}\frac ZY\Phi_N C\,d\mu
=
\Omega\int_{\mathbf Z_p^\times}x^{-1}\,d\nu_{N,C}(x).
\quad}
\tag{15}
\]
这里完整的负一 Mellin 算子没有被积分掉或换成正矩。
(15) 保原单位域。

同一论证适用于原 e0/e1/e2 的每个合法 tensor 项，
故对 G4 上的全部混合有限门准确成立。
\(\nu_{N,C}\) 可以含完整34维及 torsion-translated blocks；
没有理由只保 R735 的 D2/D4，也没有理由只保裸 W 型五的11维。

## 6. 完整返回分母：代数有限化可以做，degree 成本不能删

对 R737 的 V/W 返回，原观察为
\[
Y_\kappa^V=(\kappa V+\alpha W)/36,\qquad
Y_\kappa^W=(V+\alpha\kappa W)/36,\qquad
N(Y_\kappa^V)=N(Y_\kappa^W)=34.
\tag{16}
\]
整个 \(\kappa=\pi_0/\bar\pi_0\) 保留，不截成首项。
相应 \(z_V,z_W\) 与各自 \(Y_\kappa\) 正交；
其余伙伴及 \(\Phi_N\) 按同一个原 unitary 变换运输。
全部门在固定 p、\(\ell\) 后仍是有限 p 门，
包括移动 E 门、W/V unit 门和原两分支。

这些行的系数可以不是 \(\mathcal O_K\) 中的整数。
取一个实际清分母元
\[
d=36\bar\pi_0\in\mathcal O_K,\qquad
Y'=dY_\kappa .
\tag{17}
\]
它在所选 ordinary p 处是单位；
对 (16) 两支都足以清分母。
其真实 index 为
\[
\boxed{\quad
N(Y')=34\,N(d)=34\cdot36^2p .
\quad}
\tag{18}
\]
可以在额外原同余已支付时约去公共因子，
但本篇使用这个始终有效的显示成本。
不能仅由 \(N(\kappa)=1\) 就把非整行在原格上的截面免费称作 degree34。

对整行 \(Y'\)，§2–5 的外张量及有限 jet 论证照用，
保它的实际 flat twist、原全部 theta lift 及 (18) 的 index。
因为 d 是所选 p 处单位，
\[
Y_\kappa\ {\rm unit}\Longleftrightarrow Y'\ {\rm unit},
\qquad Y_\kappa^{-1}=d(Y')^{-1}.
\]
故完整返回积分有准确形式
\[
\boxed{\quad
\int\frac{z_\kappa}{Y_\kappa}\Phi_N C_\kappa\,de_1
=d\Omega\int_{\mathbf Z_p^\times}x^{-1}
                  \,d\nu'_{N,C_\kappa}(x),
\quad
\nu'_{N,C_\kappa}
=\Omega^{-1}(Y')_*(z_\kappa\Phi_N C_\kappa e_1).
\quad}
\tag{19}
\]
右端仍是有限代数 theta 来源的原负一单位矩。
所有数 \(d,\lambda,\kappa,u\) 均为已指定的代数数。
也可以将这个来源放回相应 adelic p-isogeny/Schwartz 模型，
但必须保 (18) 所记录的实际层变化及其转模因子。

(19) 同时保整个有理分母和所有质量；
它不需要将 \(z_\kappa/Y_\kappa\) 展开成无限 \(\kappa\)-级数。
若另用 R740 的级数，所有项合起来必须与 (19) 相同。
本篇没有据此将返回改成 E24 负一行；
其 Y 型十七 gluing 继续存在。

## 7. 给点公式的准确输入

本篇已证明：在固定 p 和有限门层上，
R737 的实际 G4 及两条完整返回都可先有限化为
\[
\Omega\times
 \text{有限个代数系数的、带原 torsion/level 的 theta 负一单位矩}.
\tag{20}
\]
这里不是将一个无穷条件积分的系数猜成代数数。
证明使用完整有限 Fourier 和、原相位、代数 torsion jets
及所有齐次周期相消。

若一组原参数的门层固定、theta 模型及多项式次数固定，
而只有已付代数系数随参数变化，则上述展开可以选同一个有限来源池。
这项有限性本身不把参数极限的任意 p 进数变成代数数；
实际极限仍须用原系数公式另行支付。

下一步仍须：

1. 对 (20) 中全部实际 theta/Schwartz 分量建立同周期的负一算术公式；
2. 若使用 R746，先证明相应分量确在其两条 Hecke 来源及真实有限扭的范围；
3. 核实际点坐标域，尤其 R744 中 E2312 所需的二处条件；
4. 保整个 G4、两个返回、所有质量及原各自外部的同一线性身份。

系数的代数性不等于点域不分歧，也不等于负一值非零。
因此本篇未由 (20) 宣称主中央或主目标完成。

## 参考

- [R686](R686-original-yz-core-and-same-source-st-unit-failures.md)、
  [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)、
  [R737](R737-common-depth-elimination-and-native-primitive-strips.md)、
  [R740](R740-original-w-v-spherical-seventeen-tensor-and-mixed-cuts.md)：
  原物理行、全部正交伙伴、混次规范和实际返回。
- Kenichi Bannai, Shinichi Kobayashi,
  *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*,
  Duke Math. J. 153 (2010), 229–295；
  [作者预印本 v4](https://arxiv.org/pdf/math/0610163)。
  本篇引用的编号按该 v4：Theorems 2.9、2.12，Propositions 1.14、2.19，
  尤其 Prop.2.19 第一式的完整配对、偶阶基点提升与 torsion 代表相容性。
