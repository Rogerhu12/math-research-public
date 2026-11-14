# R178. 实际共同平移 $3D_b$、典范函数与完整初始运输

日期：2026-11-13。**状态：已证明（完成范围为实际除子恒等式、两个完整整理想、24步短组合与两个初始运输范数；共同304位链及完整全局高度尚未完成）。**

本结果给出实际共同平移 $3D_b$ 的准确除子恒等式及其主函数规范，构造 $B_8,U_b$ 的完整整Makdisi理想，并已完成24步短组合、保存每一实际主截面。下面将数学恒等式、已完成的实际理想和短组合运算分别标明；新的304位乘法、形式终点运输和完整全局高度不在当前完成声明中。

## 1. 真实除子与规范

沿用R117同一基除子
$$D_0=K_f+D,\qquad\mathcal L=\mathcal O(D_0),\qquad\deg D_0=126,$$
其中 $D$ 是20个约化尖点，$f=f_0$ 是R110已固定的典范截面。实际点
$$B_4=Z_{-4}-D,\quad B_8=Z_{-8}-D,\quad U_b=20b-D$$
都保持整数除子规范。R112给 $B_4=[K_f+Z_{-4}-D_0]$，没有丢掉挠点。

R148/R151改用实际典范除子 $K_{g_1}$ 后，两个CM点共享
$$D_b=162u+8b-27Q_2+4K_{g_1},\qquad Q_2=2c+Z_{-8},$$
其中 $b=P_{-3},u=P_{-12},c=P_{-7}$。确有
$$D_P=F_2(P-b)+D_b,\qquad F_2=27T_2+4.$$
这里 $\deg D_b=162+8-27\cdot22+4\cdot106=0$。

## 2. 典范关系由一个明确函数实现

令 $S_0$ 是 $j=0$ 上除唯一阶三椭圆点 $b$ 外的约化支撑，$S_2$ 是 $j=1728$ 上除20个阶二椭圆点 $Z_{-4}$ 外的约化支撑。实际 $j$ 映射的次数为820，尖点宽度41，因而
$$\operatorname{div}j=3S_0+b-41D,$$
$$\operatorname{div}(j-1728)=2S_2+Z_{-4}-41D,$$
$$\operatorname{div}(dj)=2S_0+S_2-42D.$$
最后一式逐个粗模分歧点微分得出；曲线在其他点不分歧。次数核对为 $\deg S_0=273,\deg S_2=400$，所以 $\deg\operatorname{div}(dj)=106$。

对任一明确全纯微分 $\omega$，令 $K_\omega=\operatorname{div}\omega$，定义实际有理函数
$$R_\omega=\frac{(dj/\omega)^6}{j^4(j-1728)^3}.$$
三式相减给出**除子群中的等式**
$$\boxed{\operatorname{div}R_\omega=35D-3Z_{-4}-4b-6K_\omega.}\tag{2.1}$$
所以R110的 $6K\sim35D-3E_2-4E_3$ 在这里不仅是一个Picard类关系；所用主函数已经给定。

更重要的是，R123的同一不变微分 $dx/(2y)$ 和Kodaira–Spencer规范给这个函数直接求值。对 $E:y^2=x^3+Ax+B$，置 $\mathcal D=4A^3+27B^2$，令 $W_\omega$ 为同一weight2截面的实际数值。由R123式(123.6)，
$$\omega=W_\omega\frac{9B\,dA-6A\,dB}{2\mathcal D},\qquad
j=\frac{6912A^3}{\mathcal D},$$
故
$$\frac{dj}{\omega}=\frac{124416A^2B}{\mathcal D W_\omega}.$$
因为
$$\frac{124416^6}{6912^4(-46656)^3}=-16,$$
得到准确恒等式
$$\boxed{R_\omega=\frac{-16(4A^3+27B^2)}{W_\omega^6}
=\frac{\Delta_E}{W_\omega^6}.}\tag{2.2}$$
它保留了真实尺度，不是差一个待拟合常数。改变短模型的坐标时，分子和分母都按weight12改变，故商下降到实际模曲线。

在 $b$ 处原weight2截面含 $A^2$，粗参数是 $A^3$；在 $Z_{-4}$ 处含 $B$，粗参数为 $B^2$。若 $\omega$ 在相应粗模点为单位，(2.2) 的极阶分别为四和三；一般情形额外的极阶正是 $6K_\omega$。这与 (2.1) 的粗模重数完全一致。

在当前所有Abel族的实际模型 $A=1,B=32+t$ 上，(2.2) 直接成为
$$R_{g_1}(t)=\frac{-16(4+27(32+t)^2)}{W_{g_1}(t)^6}.$$
已有实际weight2三阶展开即可求其模47四位的形式范数；无需再求41挠点或新的模函数。

若 $h_g=g_1/f_0$，则必须保留
$$\boxed{R_{g_1}=R_{f_0}h_g^{-6}.}\tag{2.3}$$
源码同时保存 $g_1$ 在实际73维基中的系数和 $f_0$ 系数。典范证书中的54维系数先经R110的典范包含矩阵嵌入；没有把54维向量与73维取值直接配对。

## 3. 五个整数点的准确组合

由 (2.1) 和 $Q_2=2c+Z_{-8}$，直接展开得到
$$\boxed{3D_b=486(u-b)-162(c-b)-81B_8-6B_4+17U_b-2\operatorname{div}R_{g_1}.}\tag{3.1}$$
每个系数可在除子群中逐项核对：右边的非主部分为
$$486u+16b-162c-81Z_{-8}+70D-6Z_{-4},$$
减去 $2\operatorname{div}R_{g_1}$ 后恰为 $486u+24b-81Q_2+12K_{g_1}=3D_b$。

两条CM链已有的真正初始代表是
$$A_{12}=(u-b)+\operatorname{div}h,\quad
A_7=(c-b)+\operatorname{div}h,\qquad h=f_b/f_0.$$
因此用五个实际初始代表组成
$$P_{\rm comb}=486A_{12}-162A_7-81B_8-6B_4+17U_b$$
时，有
$$\boxed{P_{\rm comb}=3D_b+\operatorname{div}(R_{g_1}^2h^{324}).}\tag{3.2}$$

短组合按真正AddFlip记录函数 $F_{\rm build}$，满足
$$\operatorname{div}F_{\rm build}=P_{\rm comb}-A_{\rm new}.$$
所以最终点的准确初始运输是
$$\boxed{h_D=R_{g_1}^2h^{324}/F_{\rm build},\qquad
A_{\rm new}=3D_b+\operatorname{div}h_D.}\tag{3.3}$$
结合 (2.3)，同一公式也写成
$$h_D=R_{f_0}^2(g_1/f_0)^{-12}h^{324}/F_{\rm build}.$$
这就是保持R112/R117旧基除子、同时使用R148新典范代表时的完整规范。

下一条 $m$ 链若给 $\operatorname{div}F=mA_{\rm new}-A_{\rm old}$，再给实际终点函数 $\operatorname{div}g=A_{m(3D_b)}-A_{\rm old}$，则
$$\boxed{f_D=F/(g h_D^m),\qquad
\operatorname{div}f_D=3mD_b-A_{m(3D_b)}.}\tag{3.4}$$
所有后续高度都显式保留这里的3；3和 $m\equiv9$ 在47处均为单位。

## 4. 两个新完整理想已经算出

`p41_translation_points47.py` 从R160同一73维归一化参数和71条全局二次关系，使用同一个73阶单位Jacobian，将 $b$ 的展开从0..16阶延伸到0..19阶。原17个系数逐项一致；所选全局关系、$f_0=1$、参数条件及实际Frobenius下降全部核对。

71个方程的Jacobian在曲线点的横向满秩；再加 $f_0=1$ 与所选参数，给单位方阵。R160已识别该光滑形式支就是实际曲线，因此延伸具有唯一性，并非另选同维形式曲线。

R110的 $I_K=H^0(2\mathcal L-K_f)$ 秩93。在CM8的20个真实点施加取值条件，得到
$$H^0(2\mathcal L-K_f-Z_{-8});$$
在 $b$ 施加0..19阶条件，得到
$$H^0(2\mathcal L-K_f-20b).$$
两次限制都准确为秩20，并保存20阶单位子式及逆，故得到完整73维整理想。在 $R_2$ 的 $(1,i)$ 基中，两子式行列式分别是 $(3590928,3691879)$、$(1768494,234735)$ 模 $47^4$；证书同时保存其完整逆。剩余次数126大于 $2g-2$，且不小于 $2g+1$，Riemann–Roch与全局生成性证明公共零除子分别恰为 $K_f+Z_{-8}$、$K_f+20b$。

按同一基除子 $D_0=K_f+D$，它们分别表示实际整数点 $B_8,U_b$，没有除法或未知挠点。

已完成的231003字节证书：
`/tmp/p41_translation_points47_checkpoint.json.gz`，SHA256
`55279f5bd497c34abc1047b105cdf4c480ff3bf062ad42d7488b485a90422002`。

完整点SHA：

- B8：`b9fb37ae561ae8c1be91acd28dfbefea82d3c3181c7d2ecff8e34d07f64678eb`；
- U_b：`f1d481c3c16d55f7ba82718300a0b6118613495569fe73674d7acdc9bb7201af`。

实际耗时15.6秒，峰值91.4MiB。源码仅用既有准确整数矩阵，不调用GP。

## 5. 已完成的短组合与完整主函数

`p41_translation_build47.py` 使用与CM7完全相同的819点评价图，删去初始CM7所在第254行。所有群操作最大截面次数630，小于819，实际等式仍由全部评价点忠实检测。二次/三次基变换哈希与已发布CM7链逐项一致；所有保存的点和函数系数都转回原R102/R110基。

五个系数 $(486,-162,-81,-6,17)$ 的联合二进制程序固定为8次double、15次add，再一次末尾flip，共24步。CM12/CM7/B4的准确负点及主函数直接复用已发布数据；只为B8/U_b新算负点。每步都保存完整实际二次或三次截面和函数递推：
$$F_R=(F_PF_Q(s/f_0^3))^{-1};$$
末尾flip用 $F_R=(F_P(s/f_0^2))^{-1}$。每个负基点的函数是其二次负点截面的逆。

函数递推可在除子群中直接归纳验证。若当前整数表达式为 $v$，保持不变量 $\operatorname{div}F_P=\sum_i v_iA_i-A_P$。真正AddFlip主截面满足 $\operatorname{div}(s/f_0^3)=A_P+A_Q+A_R$，所以新函数的除子是 $-\sum_i(v_i+w_i)A_i-A_R$，与记录的整数表达式 $-(v+w)$ 相同。负基点的 $q_i/f_0^2$ 满足 $\operatorname{div}(q_i/f_0^2)=A_i+A_{-i}$，故取逆正好给表达式 $-A_i$。最后一次flip的二次主截面同理。这个归纳证明最终 $\operatorname{div}F_{\rm build}=P_{\rm comb}-A_{\rm new}$，不是只靠最终点类或矩阵迹吻合。

每一步后将整个当前点、Frobenius、整数系数向量、实际函数系数和随机状态原子写入
`/tmp/p41_translation_build47_rolling.json.gz`。已有第7步固定证书时，在课题目录用以下命令于独立路径重现全部24步，不覆盖任何正在运行的rolling：

~~~
cp scripts/data/p41_translation_build47_7_fixed.json.gz /tmp/r178-build-replay.json.gz
python -B scripts/p41_translation_build47_finish.py --script-dir scripts --points scripts/data/p41_translation_points47_checkpoint.json.gz --checkpoint /tmp/r178-build-replay.json.gz
~~~

从头重建新点则运行 `python -B scripts/p41_translation_points47.py --script-dir scripts`。原短构建器可从空检查点重新运行同一算术；由于驱动历史元数据不同，完整JSON的摘要会不同，但实际点和主截面相同。上述从第7步使用同一恢复器的路径则保留最终证书的元数据。短组合初期实测峰值164MiB；恢复器峰值143.06MiB。

短组合现已完整通过24/24步。最终固定文件 `p41_translation_build47_complete.json.gz` 为775018字节，SHA256 `80126f2679fe969fbe1c83dd6ecbc0ff4490871310b5d4304945232308b95f33`；实际 $3D_b$ 初始点SHA为 `157e08949b4cb8a367e9d83927494fb92674aa33093daca05bbe87a5f24500b7`。全部24个主截面系数的独立摘要重组均一致，末尾整数表达式准确为 $(486,-162,-81,-6,17)$。恢复后的实际耗时约668秒，峰值143.06MiB。新的共同长链和终点高度仍未完成。


## 6. 本次内存恢复的固定边界

短组合在第7步原子检查点之后遇到进程137终止，没有丢失任何已写步骤。原构建器不改动；`p41_translation_build47_finish.py` 仅在群操作循环前释放不再使用的解码JSON和原820点评价矩阵，使用完全相同的实际点、主截面基、运算顺序与已存随机状态，并在检查点记录新旧驱动SHA。

不可变恢复点为 `p41_translation_build47_7_fixed.json.gz`，7/24步，614560字节，SHA256 `96d3c6c054e4a46e4901984923c9ed4a7ebab3cdbf02290f9f53cfbefb35eb4e`。从它复制到rolling后，可用低内存恢复器续算，不能把原构建器或恢复器的不同源码SHA隐藏成同一个程序。

内存恢复时，CM12从完整145位/217步边界继续，CM7完整120位/180步已固定。为了控制内存，CM7在共同短组合完成前暂缓恢复；这不改变其已有点、函数、随机状态或运算计划。新的共同304位链尚未启动。


## 7. 精确数学接口与可复验边界

本结果的关键区别是 (3.3) 在实际除子群中成立。输入的 $B_4,B_8,U_b$ 是固定整数除子；$A_{12},A_7$ 的主函数 $h=f_b/f_0$ 已明确；(2.2) 固定了典范关系的实际乘数；短组合保存 $F_{\rm build}$ 的完整直线程序。因此从它产生的后续范数必须计算 $F/(g h_D^m)$，不能只用短组合点类或仅用新的304位主函数 $F$。

在 $R_2=(\mathbf Z/47^4)[i]/(i^2+1)$ 上，所有矩阵只使用单位子式作逆。CM7评价图删除第254行后仍有819个实际评价点；需要判等的截面次数至多630，所以全部评价点上的等式是真正曲线上截面的等式。每次AddFlip的余除子计算和Frobenius下降使用R117的完整整理想算法。保存的系数始终转回R102/R110的原二次或三次截面基；改变评价图未改变后续有理函数的规范。

所有NumPy整点积都先在模 $47^4$ 的代表上归一，涉及的整行累加长度不超过820。实部或虚部的绝对值统一由 $2\cdot820(47^4-1)^2<2^{63}$ 控制，故没有int64溢出造成的伪同余。

初始理想证书保存两次20阶单位子式及其逆、完整73维核、实际Frobenius矩阵和20阶 $b$ 盘展开。短组合证书保存24步的运算计划、当前真实点、每个二次/三次主截面系数与SHA、整数表达式和随机状态。可恢复驱动更换单独记录在 `driver_history`，不改旧SHA。

### 引用与原始规范

- [R110](R110-actual-cusps-and-canonical-divisor-ideals-at47.md)：尖点、典范包含矩阵、$D_0$ 与真实截面基。
- [R112](R112-actual-cm-minus4-class-in-local-makdisi-model.md)：$B_4=Z_{-4}-D$ 的整数代表。
- [R117](R117-actual-cm-group-operations-and-principal-poincare-norm-at47.md)：真实AddFlip、负点、主截面和Frobenius规范。
- [R123](R123-actual-weierstrass-differentials-and-formal-logarithm-scale.md)：$dx/(2y)$ 与Kodaira–Spencer的精确尺度，直接用于 (2.2)。
- [R148](R148-global-correspondence-section-with-diagonal-and-basepoint.md)、[R151](R151-complete-miller-local-connection-and-cm-norms.md)：$F_2$、$Q_2$、$D_P$、$K_{g_1}$ 和实际全局截面规范。
- [R154](R154-double-miller-transport-and-hecke-reuse.md)：双变量主函数运输和真实Hecke范数的方向。
- [R159](R159-integral-weierstrass-cancellation-and-exact-jet-precision.md)、[R160](R160-actual-canonical-algebras-cm-discs-and-integral-miller-cancellation.md)：后续非单位局部因子的正确处理；本结果不以数值除47损失精度。

## 8. 共用一条平移链的完整双变量公式

本节给出后续计算的精确接口，不把尚未构造的函数标为已知数值。固定 $P=u$ 或 $c$，写 $C=P-b$。第一变量使用原family0实际代表 $A_Y$ 和函数
$$\operatorname{div}f_{C,0}=mC-A_Y.$$
为避免第二变量最终支撑与 $A_Y$ 相交，另选实际Abel族 $S$，并用真实换框函数构造
$$\operatorname{div}f_{C,S}=mC-A_S.$$
更明确地，若 $\operatorname{div}h_{0S}=A_S-A_Y$，则 $f_{C,S}=f_{C,0}/h_{0S}$，不是默认两个局部框架相同。
设实际Hecke换框函数、共同链的最终函数分别满足
$$\operatorname{div}\rho_T=T_2A_S-A_T,\qquad
\operatorname{div}f_D=3mD_b-A_{D_b}.$$
这里 $\rho_T$ 的取向与R170相同。再用短形式群组合的真实主函数 $F_\Sigma$，使
$$\operatorname{div}F_\Sigma=81A_T+12A_S+A_{D_b}-A_Z,$$
其中 $A_Z$ 是 $3mD_P$ 在family1的明确代表。于是
$$\boxed{g_P=\bigl(\operatorname{Norm}_{T_2}(f_{C,S})\rho_T\bigr)^{81}
f_{C,S}^{12}f_DF_\Sigma}\tag{8.1}$$
满足
$$\operatorname{div}g_P=3mD_P-A_Z.$$
证明只需逐项取除子：范数项给 $mT_2C-T_2A_S$，乘 $\rho_T$ 后得到 $mT_2C-A_T$；81和12分别等于 $3\cdot27$、$3\cdot4$。随后共同项和 $F_\Sigma$ 准确消掉全部中间代表。因此没有隐藏的第二条304位Hecke链，也没有把 $T_2A_S$ 的Picard类相等替代实际范数。

设R148/R151的规范全局截面在R175的真实 $j$ 参数生成元中是
$$\sigma_{F_2,b}(P)=s_P\,e_j(C,D_P).$$
对R175的第一变量搬运再乘 $3m$，然后对第二变量应用R154，得到
$$\boxed{
3m^2\lambda_{47}(\sigma_{F_2,b}(P))
=3m^2\log_{47}s_P+\lambda_{47}(e(A_Y,A_Z))
+3m\log_{47}f_{C,0}[D_P]_j+\log_{47}g_P(A_Y).
}\tag{8.2}$$
其中 $A_Y$ 和 $A_Z$ 分别在同一R141的family0和family1。只有当它们与各次函数支撑的实际不交性已核准时，末项才可直接按普通范数相乘；否则必须按R159保留整盘因子，不能除掉47而丢失精度。$f_{C,0}[D_P]_j$ 是R175证明的碰撞修正广义范数。

式(8.2) 中 $m\equiv9\pmod{47}$，故 $3m^2$ 为47进单位，不损失四位精度。最后R148原QC右端仍是 $800\lambda_{47}(\sigma_{F_2,b}(P))$。式(8.1)–(8.2) 明确了所有待算量及其方向，但本节不声称这些范数或完整高度已完成。

## 9. 已完成的两个初始运输范数

在R167两个已验证的 $A_Y=A_{\rm family0}(mC)$ 上，实际范数只需54个移动点与其固定原点；共同72点在除子中准确相消。使用同一 $A=1,B=32+t$ 模型的真实三阶展开，将 $R_{g_1}$、$h$、五个负基点二次主函数以及全部24个短组合主截面逐项代入。每个分子和分母在整个相应剩余盘都是单位，所以参数在 $47R_2$ 上的三阶代入确实保留模 $47^4$ 的全部值。

所有乘积按实际Frobenius配对下降到 $\mathbf Z/47^4$，范数均为 $1\pmod{47}$。下表均为模 $47^4=4879681$ 的准确整数：

| 第一变量实际族 | $N(R_{g_1})$ | $N(h)$ | $N(F_{\rm build})$ | $N(h_D)$ | $\log_{47}N(h_D)$ |
|---|---:|---:|---:|---:|---:|
| $A_{\rm family0}(mC_{12})$ | 3193369 | 4836959 | 2414391 | 229643 | 3651383 |
| $A_{\rm family0}(mC_7)$ | 2683231 | 3598180 | 3726772 | 1358348 | 4040073 |

程序分别核对
$$N(h_D)=N(R_{g_1})^2N(h)^{324}/N(F_{\rm build}),$$
$$\log N(h_D)=2\log N(R_{g_1})+324\log N(h)-\log N(F_{\rm build}),$$
并从 $R_{f_0}$ 和 $g_1/f_0$ 独立重组 $N(R_{g_1})$。因此表中数值包括真实典范换框，没有丢掉 $-12$ 次幂。

实现为 `p41_translation_initial_norms47.py`。它使用已发布R145紧凑证书中的同一家族、已发布820点真实三阶展开及R167目标；各自所绑定的原始Abel-bases和jets SHA逐项一致。程序不依赖未保存的大Hecke评价矩阵，不重复任何304位群运算。

最终3046字节小证书为 `scripts/data/p41_translation_initial_norms47_checkpoint.json.gz`，SHA256 `ebd03003cf89a92bc58585a1458bd0a260c50e269bec594ea8fe1a89aacec315`；生成源码SHA为 `11c193f412699156246da436ce89566dce7c0120362cc487066cbafb4dec937e`。从课题目录可直接复验：

~~~
python -B scripts/p41_translation_initial_norms47.py --script-dir scripts --build scripts/data/p41_translation_build47_complete.json.gz --output /tmp/r178-initial-norms-replay.json.gz
~~~

这次完整计算耗时17.28秒，峰值96.35MiB。此前原始Abel-bases输入的计算与最终已发布紧凑输入版本给出完全相同的两条逐步范数记录；最终证书采用后者，因而从仓库恢复无需依赖临时raw文件。

这些值是共同链初始主函数的实际范数。最终式(8.2)仍需共同链的 $F_{\rm chain}$、真正终点换框、两CM碰撞广义范数、实际Hecke范数和最终形式纤维；不能把本表当成完整高度。
