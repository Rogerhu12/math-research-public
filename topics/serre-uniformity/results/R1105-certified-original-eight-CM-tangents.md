# R1105 — 原八个CM点的十六个实际整切向读数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明（完整有限精确计算）。**

## 1. 结论

取 [R1074](R1074-certified-original-p47-eight-CM-disks.md)、
[R1086](R1086-certified-original-p47-ell4513-same-CM-transfer.md)
已识别的原 $Y=X_{\mathrm{ns}}^+(47)$ 的八个有理CM点。
在 $q=4513$，令每点的实际粗模参数为
$$
z=j-j(y),\qquad
\omega_i=e_{y,i}\,dz+\text{正阶项}.
$$
$\omega_i$ 是 R1093 规定的十六个原一次 Hecke 块的规范微分；
其原 Hodge 坐标第一个非零项为1，完整坐标哈希固定。
记
$$
P_0=B_qu_4,\qquad
\lambda_{4,i}=q^{-1}\log(P_0)(\omega_i)\pmod q.
$$
本次实际计算支付全部 $8\times16$ 个
$$
\boxed{\quad b_{y,i}=e_{y,i}/\lambda_{4,i}\in\mathbf F_{4513}.\quad}
\tag{1105.1}
$$
**全部128个 $e_{y,i}$ 都非零，故全部128个 $b_{y,i}$ 都是单位。**
旧 $\lambda_{4,i}$ 直接消费，未重算高CM对数。

作为具体原坐标，$H_2=T_2+2T_3+4T_5$ 标签434的
$\lambda_{4,434}=3527$。下表给八个此坐标的实际值，
以及执行中用到的真实模型/域范围：

| 原候选id | 有理 $j$ | $j\bmod4513$ | 完整47挠域次数 | 实测候选项链数 | $e_{y,434}$ | $b_{y,434}$ |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 16 | 1 | 2818 | 345 |
| 76 | -3375 | 1138 | 4 | 25 | 2115 | 3124 |
| 77 | -12288000 | 899 | 16 | 1 | 983 | 1038 |
| 100 | 16581375 | 613 | 4 | 25 | 3476 | 4125 |
| 108 | 8000 | 3487 | 48 | 1 | 2364 | 2634 |
| 141 | 1728 | 1728 | 1 | 1 | 4304 | 1680 |
| 196 | 287496 | 3177 | 4 | 25 | 4174 | 69 |
| 220 | 54000 | 4357 | 16 | 1 | 2887 | 3526 |

其它十五个规范一次块的每点完整行也在成功日志中，
其逐点SHA列于§5。结论不以一个块的非零替代其余十五个块。

### 1.1 Frobenius 纤维的精确说明

候选196、$j=287496$ 的实际模型虽为普通约化，
其迹为94，模47仍是0，故原 routine 实际枚举25条项链。
候选76和100的超奇异模型迹为0，也各枚举25条。
其余非Gaussian模型分别枚举一条；
Gaussian直接消费已固定原Cartan及Weil基。

因此方法§1中“ordinary nonsplit fiber一条、两个SS纤维25条”的
概括不能理解为所有普通模型都只有一条。
**实际判据始终是原Frobenius矩阵，代码在三种25条情形都做完整原tag匹配。**
本次每个模型恰一条匹配，未删普通trace94这一分支。
这项说明不改变任何计算式或成功数值。

## 2. 原几何尺度的证明

### 2.1 项链、Weil根和同一Reynolds源

原235标签由旧消费者按旧字符与粗点哈希重建，只作为输入；
新任务仅取固定八个CM记录，没有重新执行完整5453点筛选。

旧标签使用 $J^2=5I$，原Hodge使用 $I_0^2=-I$。
消费者先按旧 native Weil根、全部 $\psi_5$ 轨道、
圆单位角色和原零角色完整比较tag；
唯一匹配后才用 $I_0=13J$ 换到Hodge标记。
以实际椭圆加法求 $I_0P$，再作
$$
(P,I_0P)\longmapsto(rP+sI_0P,\,-sP+rI_0P)
$$
的范数缩放，将实际 $e_{47}(P,I_0P)$ 调为2。
完整Weil配对被直接检查，没有仅用一个未标定行列式替代。

所有2208个非零47挠点的原weight-one值由同一链
$1,2,4,5,10,11,22,23,46$ 和真实短Weierstrass斜率读取。
若 $Y^2=X^3+AX+B$，取原微分 $dX/(2Y)$，
则原 $47e(P)$ 等于该加法链的负斜率和。
全格检查奇性、无点碰撞及与Frobenius相容。

95个实际描述子 $(a,c,d)$ 使用
$$
G_{a,\rho}
=\sum_{x\ne0}\left(2^{aN(x)}e_xe_{\rho x}
                 +2^{-aN(x)}e_xe_{\bar\rho x}\right),
\qquad \rho=d+ci .
\tag{1105.2}
$$
实/虚方向、两个phase、纯虚 $\rho$、
46个范数类及每类24个半向量全保留。
半格乘二是原偶乘积恒等式，不是省略一半来源。

### 2.2 粗模参数与短heat

设 $D=4A^3+27B^2$。R1103 的原Kodaira–Spencer式为
$$
\mathrm{KS}=\frac{9B\,dA-6A\,dB}{2D},\qquad
dj=\frac{124416A^2B}{D}\mathrm{KS},\qquad
\omega_F=F\,\mathrm{KS}.
\tag{1105.3}
$$
因此在generic点，
$$
e_F=\frac{D}{124416A^2B}F.
$$
Gaussian、cubic 的完整粗尺度分别是
$$
e_F=-\frac{\partial F}{41472A}\quad(B=0),\qquad
e_F=\frac{\partial^2F}{331776B}\quad(A=0).
\tag{1105.4}
$$
所选 canonical CM Cartan 含完整椭圆稳定子；
原j-map在这两个粗点的参数正是上式的参数。
Gaussian的 $F(0)=0$、cubic的 $F(0)=\partial F(0)=0$
逐个描述子实际检查，不能再额外乘或除2、3。

heat在 $A_2=0$ 截面计算，但求二阶时保
$\partial A_2=4A$。具体原式
$$
\partial e=-xe-y,\qquad
\partial^2e=-2e^2y-4x^2e-2Ae-2xy
$$
由完整原系统取得。乘积二阶用
$F''G+2F'G'+FG''$；输出是真导数，不把Taylor系数与导数混用。
generic/Gaussian/cubic只读0/1/2阶。

模型同构 $(x,y)\mapsto(c^2x,c^3y)$ 下，
$F,\partial F,\partial^2F$ 分别乘 $c^2,c^4,c^6$；
(1105.3)–(1105.4)中的系数分别乘其逆。
故所得 $e_F$ 是实际粗参数的值，不依所选短模型尺度。
项链的原tag与实际Weil根则另按§2.1固定。

### 2.3 接回原73维格和十六个块

原95来源、全部23 cusp留数及73维整核按R1090已证证书消费。
原 $T_2,T_3,T_5,H_2$ 的实际行作用矩阵逐项核原哈希。
对每个旧 $H_2$ 根，重建一维左特征空间，
按首非零坐标归一并核R1093特征向量哈希。

设原核矩阵为 $K_{\mathrm{hol}}$、特征行矩阵为 $V$，
则实际投影是
$$
(e_{y,i})_i=V K_{\mathrm{hol}}(e_{y,\lambda})_{\lambda=1}^{95}.
\tag{1105.5}
$$
这全在原 $X_{\mathrm{ns}}^+(47)$ 的整格内进行。
对 $[x-y]$ 的切向没有额外23；
旧 $B_q$、CM周期及 $\lambda_{4,i}$ 也没有被删除。
(1105.1)于是是R1103同一原MW坐标的真实切向。

## 3. 原生库故障与完整成功范围

第一次
run45965927561/job140394474708、source
c24a2dd1f433f8fa459e1f9a13cde41d6c028d04
只完成旧Hodge和235标签输入，随后在第一次有限域构造时exit139，
未给出任何CM点值。真实栈为python-flint扩展解析到了已加载的
Sage FLINT库；不是数学等式失败。

v2将Sage矩阵和python-flint域运算放在两个exec隔离进程。
原数学函数逐字未改。子进程不import Sage，
运行时loader回执只含wheel自己的libflint24；
父进程只接收已经过Frobenius与常数坐标检查的95个
$\mathbf F_{4513}$ 整数及其SHA，再作(1105.5)。
两进程共用父开始后570秒的绝对截止，未重复取得预算。
逐点输出保证未完成点不会混入成功前缀。

最后完整成功的是
[run45968484065](https://github.com/Rogerhu12/math-research-public/actions/runs/45968484065)，
job140402824955，source **9fba1d2b2865407f949a81a72568a9980e378a3c**。
实际数学 **11.858319434秒**；请求600秒、预留30秒。
八点顺序141、0、76、77、100、108、196、220全完成。
root实读完整成功状态、逐点记录与最终回执，
将移除输出层kind/计时字段的八条记录按canonical JSON核得同一SHA。

没有重算高CM对数、旧完整辅助筛选或已成高度。

## 4. 可重现入口

- [消费者](../scripts/full_p47_eight_CM_tangents.py)；
- [方法及完整旧输入说明](../notes/2026-11-27-full-p47-eight-CM-tangents-method.md)；
- [请求v2](../notes/full-p47-eight-CM-tangent-request.json)；
- 原R1090/1093/1103来源与固定Sage10.6 image见请求和preflight。

只保脚本、参数、真实run/job和哈希；
可重算挠点格、95维/73维数组和日志不另存入仓库或Release。

## 5. 哈希

| 对象 | SHA-256 |
|---|---|
| v2脚本 | c0932538657b87e6f2c31c0d32189383fd72e65267cf20986630d73dece1f1a5 |
| v2方法 | e3b5a732579c15f4bbced8156bb12d661b9c3567077d12c3190490283cab0c51 |
| v2请求 | 9bb7b3745fc680cb89e14e94c64480dc971259be41f3068b0074c22f3561f657 |
| 八点最终记录 | a8ef06c1ec4425bae52115a56500d05e4bec419dc353438fd099867b25dd8c7a |
| 子进程95维记录 | 5ef50f1f62d3ad2b63bd1c092f214ca3cb6efe4cbfefa8cbf5b8f21b05545cd9 |

每点十六行原读数的SHA：

| 候选id | SHA-256 |
|---:|---|
| 0 | d0c574d6f72f25f6a96d8b0fb2b660d8794162ff5eea1b5dd21afaf270a8ea00 |
| 76 | ff32f70bffabf8fdff41bd99c432881718fb1b6998259b2d6caaa55fe08a8bf0 |
| 77 | e5dbe0b19a29e1d52f284e755de7d5b1528c10182d586f9f24baad753b60888e |
| 100 | c939fbf9d4c450fb3f472a6f5e849a06b00c1e88cf2e3b892557e96eab75013b |
| 108 | 7080044d782211330cb64b56efbe083e25f9db2b5d92afb09a0a467ff548ed3a |
| 141 | de10540cfa841337a473dfe7f40de824f894b6d991868da520629b64473486b8 |
| 196 | 2bdd4e602a088fdc8ab6cacfa63c53ac399a65f918f00f690c8a868118e91c4c |
| 220 | 4d26c6a511b086b324eb35b72771c953a2726e041c9a4588d0b92e5e52b621d0 |

## 6. 准确后继

本结果是八点的真实微分读数，并非有理点排除。
[R1102](R1102-certified-original-level47-complete-first-global-height.md)
已给全73维首高度，但R1103的完整QC首项还需原角作用、
有限第三类系数、CM类坐标和最终行秩/共同根判断。
尤其十六个一次块不代替全部28块的迹计算。
主目标仍须所有充分大素数的完整 Serre 一致性，继续原剩余问题。
