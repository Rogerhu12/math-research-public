# R1106 — 原23角在全73维Hecke格的实际作用与两个生成方向

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明（完整有限精确计算）。**

## 1. 新结论

取原 $Y=X_{\mathrm{ns}}^+(47)$、$q=4513$，
R1090的真实73维Hodge基和R1096的
$$
H=T_3+T_5,\qquad
\mathcal T_{\mathbf Z_q}=\mathbf Z_q[H],\qquad
P=\chi_H\bmod q,\quad\deg P=73,\quad\operatorname{disc}P=2650.
$$
本次已将R1078全部23个非恒等原角对应
$R_C$、$C=0,2,\ldots,23$，实际读成
$$
R_C=p_C(H),\qquad p_C\in\mathbf F_{4513}[X],\quad\deg p_C<73.
\tag{1106.1}
$$
完整23个多项式的系数矩阵rank为23，
原 $1+\sum R_C=0$、全部23个fixed-cycle迹、
以及全部 $23^2$ 个composition恒等式都在这个原格上精确通过。

指定原CM点为候选76、$j=-3375$。
令$e$为此点原粗参数 $z=j-j(y)$ 的73维微分值列，则
$$
\boxed{\det[e,He,\ldots,H^{72}e]=1693\pmod{4513}.}
\tag{1106.2}
$$
这支付此评价在**全部28个剩余块**上的循环性，
超出R1105仅有十六个一次块的范围。

对两个原整对称对应
$$
Z_A=13R_0+4R_2,\qquad Z_B=2R_4-7R_0,
\tag{1106.3}
$$
本次得到
$$
\boxed{\gcd(P,p_{Z_A},p_{Z_B})=1.}
\tag{1106.4}
$$
它们都Hodge-trace-zero；$Z_A$的degree为504，$Z_B$为$-72$。
(1106.4)不是说每一个方向分别在所有块上非零，
而是这两个方向没有共同零块。

在真实整Hecke代数及R1093的完整MW格$M$上，
(1106.4)进一步给
$$
\mathcal T_{\mathbf Z_q}Z_A+\mathcal T_{\mathbf Z_q}Z_B
   =\mathcal T_{\mathbf Z_q},\qquad
Z_AM+Z_BM=M.
\tag{1106.5}
$$
事实上模$q$的Bézout关系给理想商模$q$为零，
该商有限生成，再由Nakayama得整理想为一。
原角算子属于实际Hecke最大整序见R1087；
此处未只在一个有理同源模型上作生成声明。

## 2. 原几何输入与全1081目标

只消费R1105已经完成的候选76输入：
$$
E:\ y^2=x^3+786x+524,\quad
j=1138\pmod{4513},\quad a_q=0.
$$
其完整47挠域次数为4。
旧原tag在25个Frobenius固定项链中唯一选中该CM点；
实际Weil基规范为$e_{47}(P,IP)=2$、
$I=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$。
本次先核R1105的原95维coarse切向SHA，不重新证明旧筛选。

原完整几何纤维由
$$
I'=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\quad
a^2+bc=-1,\quad I'\sim-I'
$$
准确给1081个目标。每个目标取
$$
g=(v,I'v),\qquad \det g=1.
$$
程序通过各向异性二元norm表示1选取$v$，
并直接核 $\det g=1$、$I'g=gI$。
故该标记保原Weil根2，原角准确为
$C=[-\operatorname{tr}(II')/2]$。
恒等角1有一个目标，角0有24个，其余22角各48个。

全部目标共用同一原2208个挠点的weight-one值。
在目标$g$只将标签$x$重排为$gx$，
然后用原95个Reynolds描述子的两个phase作完整求和。
不改变 $\rho=d+ci$ 的实/虚方向，不删除原纯虚项、范数类或半格重数。

单个目标可能只定义在$\mathbf F_{q^4}$；
消费者保留实际扩域值，完成同一角的**全部**目标后才降域。
每个降域系数同时检查 $a^q=a$ 和非恒定域坐标全零。
这保住原对应的完整Galois轨道，没有把未定义于$\mathbf F_q$的目标丢掉。

源/目标均有同一个非特殊$j=1138$，原$j$参数在两侧étale，
底椭圆曲线及KS frame相同。
因此角和乘同一原KS-to-$dj$因子后，
再乘R1090原73维核，准确得到
$$
u_C=((R_C^*\omega_i)/dz)(y).
$$
此处没有额外isogeny尺度或椭圆稳定子重数。
标记独立性和完整Reynolds源见原方法§§2–3及R1090、R1105。

## 3. 循环评价精确决定完整算子

原角对应与away-47 Hecke对应交换：
prime-to47 isogeny运输完整47挠点标记并保角，
两种真正有限模问题的fiber product给对应交换。
R1087已把这项几何作用识别为原Jacobian上的作用。

$H$的原Hodge特征多项式平方自由、degree等于完整维数73，
所以其中央化子就是$\mathbf F_q[H]$。
故每个真实$R_C$先验有唯一(1106.1)，无需猜测抽象角域的嵌入。
由实际行作用约定，若
$C_e=[e,He,\ldots,H^{72}e]$，则
$$
C_e\operatorname{coeff}(p_C)=u_C.
\tag{1106.6}
$$
(1106.2)使其唯一可解。程序同时核
$C_eC_e^{-1}=I$以及每个原角的完整向量方程(1106.6)。

随后全部composition恒等式
$$
p_Ap_B=d_A\mathbf1_{A=B}
       +\sum_D n_{A,B}^{D}p_D\pmod P
\tag{1106.7}
$$
使用R1078已经证明的原完整系数逐对核过。
迹用同一实际Hodge矩阵$H^j$读取，与原fixed-cycle式相符，
另核
$$
\operatorname{Tr}Z_A=\operatorname{Tr}Z_B=0,\qquad
\operatorname{Tr}(Z_A^2)=336288\pmod{4513}.
$$
这些是新坐标桥的完整检查；
没有重新登记旧R1081的fiber-composition或抽象迹rank作为新结论。

## 4. 成功运行、复现与哈希

- [run45969880122](https://github.com/Rogerhu12/math-research-public/actions/runs/45969880122)，
  job140407429635，完整success。
- source **00b1f6c48d8cfd85d9920419603bef56619a249f**。
- 实际数学 **66.005069721秒**；预算1200秒、预留30秒。
- 固定官方SageMath10.6 image及python-flint0.9.0，
  Sage父进程与pure-Python域子进程exec隔离，共用同一截止。
- root实读全部24个含identity的角和回执、完整成功状态及最终证书，
  原日志的completed对象已逐字节核回输出SHA。

复现入口：

- [完整有限读取方法](../notes/2026-11-27-full-p47-original-angle-Hodge-method.md)；
- [实际消费者与复用API](../scripts/full_p47_original_angle_Hodge_action.py)；
- [固定请求](../notes/full-p47-original-angle-Hodge-request.json)。

| 对象 | SHA-256 |
|---|---|
| 脚本 | e3a8ea3ab9ecf57d2f9282afc6512b738790972f774848c922a979efa16ef4e6 |
| 方法 | 833fa0859247471585e13dbb067a0b45bceb997f5300e7cae988892371c3e170 |
| 请求 | efb681a857ccf9bf62087562431e25f7d0d160470cc0fdab545c362b339003fb |
| 完整成功结果 | 05d33f1e5dd88858ecaf19092a057ef8406c620d7fdd83d713483730c3ed9f75 |
| 原循环矩阵 | 0ab9a926a0619b85080e577c44ee3704fa7472fc1ea464ef23835ba282739f5f |
| 原73维评价列 | e3cf05d0cff74697bd418e2ee683714d83603a764c62315beedf67fcf5f6ec2f |
| 全23角的升幂坐标 | 048e083835350fb19a6edfef1e778a6cb8a965de1f472285129dc4f85ac6fb24 |
| $p_{Z_A}$ | b2b5f0ea39b29c525d26c4f60b228b73163b3e4c948b03a87b87d48ea18dc3d1 |
| $p_{Z_B}$ | 33a6d03c2bdc8ed71aedd2829ed3eed8de31a1c3d562f2343030474f3577e3c7 |

每个角的目标标记、95维求和与73维多项式哈希也在同一成功日志。
完整挠点数组、算子矩阵和可重算系数不另外提交或上传Release。

## 5. 后继消费和范围

消费者
`recover_angles(source,H,probe,field_rows,req)`
返回同一runner内的全部$p_C$；
原$\mathcal F_3^*,\mathcal F_4^*$、$Z_A,Z_B$
及其它trace-zero角组合可直接在这些实际坐标中组成。
原全73维高度已由R1102付款，八点一次块切向由R1105付款。

(1106.4)消除两个几何方向在Hecke块上同时消失的可能，
并不自动使R1103的两条QC首项行独立。
仍须实际第三类系数$\alpha$、CM类坐标和共同根判别。
本结果不宣称八盘唯一，更不宣称全$p$ Serre一致性完成。
