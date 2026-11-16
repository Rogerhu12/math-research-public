# R899 原 K 固定 trace RR 基：公开 Actions 执行契约

日期：2026-11-16。数学依据为
[完整 R899 证明](../results/R899-original-K-fixed-trace-RR-basis-from-fibre-coordinates.md)，
固定 SHA256 为
`eff6a8abf489bedf2cda8549a027ebd250717b2ddedece420f2a9d729cebc044`。
本契约只指定将来的实际运算；R894 完成来源未绑定前请求保持 pending，
不填未知 run、artifact、manifest 或原数学输出。

## 1. 唯一数学对象与成功出口

保原 $K=\mathbb Q(\zeta_3)$、$L=K(b)$ 和阶7常数域作用。
从真实完成 R894 读取
$$
T_f^0=(D_N-H)+\operatorname{div}Q_N,\qquad
W_N=H^0(3H-D_N),\quad \dim W_N=418.
$$
原正常 V3 坐标为 $B_N\in\operatorname{Mat}_{690,418}$。
正乘 $Q_N$ 标识
$$
V_K\otimes_KL=Q_NW_N,\qquad
V_K=H^0(2H-T_f^0),\quad \deg(2H-T_f^0)=544,\quad \dim_KV_K=418.
$$
输出是实际原 K 线性评价中一个418阶单位子式，以及由其完整逆定义的418个 K 固定函数。
它不要求原 $D_N$ 本身 K 固定，也不把旧正常列单独改标为 K 函数。

在辅助素数 $\ell=1000000753$ 的原地方，
$\zeta=549966761$、$s=99932770$、$B=3197390$；
不更换原六 D* 的 $[0,6,1,2,4,3,5]$ 次序和 free1186 规范。
此地方只认证特征零准确对象的单位条件，不作原41精度结论。

## 2. 所需源和实际运输

数学源组固定为 R894、R890、SIXD、R880、R887、R872、R883、R827、R885、R845。
每组保真实五元 producer identity、原完整 manifest SHA、
真实 configuration SHA、原 certificate 或原 R827 完成阶段。
所选数学文件逐 bytes/SHA 验证，旧 configuration 不改写。

- R894：真实最终证书、原 marked-QN 阶段、最终正常418、
  原 P0 正常泛函，以及16个完成节点的未缩放 u、principal 和完成小证书。
- R890：旧两步 D2/E 的同类小件、七个原正常 V3 纤维和旧源身份。
  不重旧 D2/E，不重新评价原 V3。
- SIXD：六个实际共轭的 a/v 正常坐标和 principal 小件；
  沿原同一特征零选行/自由列定义，不以新 residue kernel 代替。
- R880/R887/R872：零支原选择、v、Qf、Qtilde、共同 u_C 和 u_chi。
  原 Qf 与 Qtilde 的正乘方向、相位、阶数和标量全部保留。
- R883：真实 $c=(t/\rho)(P_0)$ 和既成首项来源，只消费，不重 jets。
- R827：原 W、地方审计、旧七个完整 K/K逆。
  原 producer 是结束的 failure/124、无 FINAL；
  仅允许它已经 complete=true 的实际指定阶段，不把整个 producer 改称成功。
- R885：已经完成的全局特征关系及旧节点0至6的七个273项关系。
  固定名字 `R885-adjugate-polynomial-characteristic-relation.json.gz`
  及其 `source_node_stages`；
  各节点含 `characteristic_coefficients_ascending_T`，不重 charpoly 或 k272。
- R845：原零支 a 在旧节点0至4的
  `section_evaluation_mod_prime[272]`，以及原 a 角色/准确列来源。

公开 wrapper 可从真实完成 R894 的源载体恢复旧七组字节；
尚缺的 R845、R885 和小叶按原已结束 producer 的 manifest 只作 Range 选择。
不得依赖开发机缓存；不得为同标签臆造旧原件；不得把完整平台 ZIP SHA 当成
Range 选件已经重新计算的哈希。运输路径不进入数学身份，所选原件身份进入。

R894 的准确 unit-solve 来源由原已认证阶段及其原引用导入；
本消费者不重新执行这些大矩阵的求核、选行或域系数重构。
原文件的 `file/bytes/sha256` 和父子指向必须原样保留。

## 3. 零支 a 的已成范围

原 R880 的 a_selection 只有角色和原点值，
不能把它当作尚未保存的690项正常向量。
首轮节点0至4直接读取 R845 已成的完整272值，不做旧乘法。

只有实际秩/分母条件需要节点5或6时，才启用一个新的小阶段：
按原 V3 权界，正常行 i 的系数次数至多 $3-\epsilon_i$。
用旧0、1、2、3四个值唯一插值最高三次多项式；
两个四阶逆乘回、全部权界和旧第4点的全部272坐标必须准确通过。
所得小阶段明确是同一原 a 的新正常多项式表示，
只用于所需缺失节点；不重复690列完整正常转换。

原 v 和六支 a/v 已有正常坐标，不进行这种插值。

## 4. 完整 Artin 运算与 QN

固定 SHA
`e47cd50d254700b98446866297d79694c100f1435c46f3b4f42e3835763f897d`
正常 import 已成 `R885_whole_Artin_algebra.py`，
只实例 `SourceAlgebra`。
不实例8维 Hecke 对应代数，不新增 Norm 算术。

在原节点 z=a 上保
$$
\mathscr A_a=\mathbb F_\ell[T]/(\bar\chi_a(T)),\qquad \dim=272
$$
的全部因子和重数。
正常向量经旧 $K_a^{-1}$ 变为循环坐标；乘后经旧 $K_a$ 返回。
每次除法都用完整多项式 xgcd 和完整乘回。
失败只记该节点的直接表达式不适用，不能改用一个几何点或伪约分。

用原 V3/V2 帧计算
$$
\widetilde Q_j=(a_j/v_j)^3\,q_C\,q_\chi^{-4},
\quad q_C=u_C/\tau^2,\quad q_\chi=u_\chi/\tau^2.
$$
共同 q_C/q_chi^4 每节点只做一次。
依 R894 的真实16步和旧两步
$$
F_{\rm new}=(qF_{\rm left}F_{\rm right})^{-1},\qquad q=u/\tau^3
$$
递推全部原 F；重复父项保两次，原 u 不归一化为1。
最后
$$
Q_N=\left(\prod_{j=0}^6\widetilde Q_j\right)F_N .
$$
只要求实际用作分母的元素为整 Artin 单位。
Q_N 本身没有被求逆，因此不预设它为单位；其零可以由后续真实秩条件处理。
所有叶、单位证书和共享标量值以源和节点缓存。
完成对象复用；未闭合的大函数表达式允许从已经完成的小叶继续。

## 5. 真实坐标归一化

新算术先得每个可用节点
$$
H_a=[Q_Nw_1(a),\ldots,Q_Nw_{418}(a)]
$$
的全部272原正常坐标。每行保准确标签 $(a,i)$。
尝试旧节点0至6，先积累三个实际可用节点；
之后若秩不足，再逐一加剩余节点。

不使用“三纤维长度大于544所以自动单射”的错误快捷推断。
只用实际全矩阵秩418，选418原行 J 并计算
$$
A=H_J,\qquad P=A^{-1}.
$$
必须保实际非零子式、两边逆乘回、全部已计算行 $HP$ 和选行单位阵。
旧七节点全部用尽仍未找到子式，只输出 false/未完成及真实节点决定。
不把它解释成不存在 K 基，不无来源另生新节点。

新正常基是 $B_NP$，而完整固定函数是
$$
\mathbf s=Q_N\mathbf wP.
$$
其准确表达由原源和 A 的指定单位逆定义；
模数组不冒称已经重构的特征零有理系数。

K 固定性由原 K 线性评价的唯一性证明。
新固定基作用矩阵准确为 $I_{418}$；
旧基作用矩阵只给 $A^{-1}\gamma(A)$ 的准确 DAG。
不计算或声称已计算另外六个模变换，不重复16flip。

## 6. 原 P0 行与供 R900 的正常纤维

保存原690项 P0 正常 V3 泛函 $\epsilon_0$，
以及418项
$$
\epsilon_0B_NP,\quad
\lambda_\rho\epsilon_0B_NP,\quad
\lambda_t\epsilon_0B_NP,\qquad
\lambda_t=\lambda_\rho c^{8435}.
$$
原极阶为8435。第一实际单位列可以作为后继未缩放标记截面；
没有观察到模单位时保持诚实 null，不从特征零非零行强填。
K 固定完整基与已成原点单位标记是分别登记的事实。

对已经计算的节点，只新乘同一变基 P，保存
`completed_normalized_space_fibres`：
正常和循环数组均272×418，明确
`original_QN_factor_included=false`。
这是 $wP$ 的正规 V3 值，不是 $Q_NwP$ 的函数值。
后继可取消共同 QN 使用它；缺少的旧节点由后继按需新算，
本 FINAL 不宣称未计算的其余纤维已经完成。

## 7. 文件、断点和失败语义

核心：
`scripts/R899_original_K_fixed_seven_trace_RR_basis.py`。

- RESULT：`R899-original-K-fixed-seven-trace-RR-basis`。
- FINAL：`p41-original-K-fixed-seven-trace-RR-basis-certificate.json`。
- CLI：`--config --retained --output --budget-minutes`。
- 数学阶段：根目录 `R899-*.json.gz`，原子 tmp 后 rename；
  `R899-current.json.gz` 为 complete=false 的真实进度。
- 每阶段完整配置同一，源表/所选件/数学策略固定；
  仅执行预算和纯运输不进入数学身份。
- stage manifest 仅列真实存在的 complete 阶段，不列自身/current。
- outer timeout 若没有 core receipt，wrapper 只记录真实不存在；
  已成阶段仍可用同数学身份完整恢复。
- false FINAL 仅历史终点，不用其旧 inventory 或 current SHA 阻止更新后的真实续算。
  true FINAL 必须逐全部活引用/源/字节核验。
- Source failed-node、rank deficiency 与 budget 是不同状态；
  completed K basis、原点标记和 downstream RR/height 各有独立旗标。

首预算300分钟不是成功声明。
核心入口拒绝在公开仓库 Actions 之外执行数学。
AST 与纯 IO 属普通实现检查，不设置独立泛型算术测试或额外审批门。

## 8. 明确没有完成的对象

R899 不给 $\mathbb Q$ 固定基，不把 $D_N$ 改成 K 定义；
不算新的有效272代表、Hecke 范数、五原 $L_j$ 的128/144空间、
Poincaré 连接、non-p 校准或高度。
准确域系数仍是原 source-bound unit-solve 表达式。
其新实际出口仅为完整 K 固定418函数基、原选行归一矩阵、
真实 P0 首项及后继可用的原正常坐标。

