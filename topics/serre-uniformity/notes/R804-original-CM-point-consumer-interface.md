# R804 原 CM 点的八节点消费者：字段、特殊点分支与实际同源像

日期：2026-11-15。状态：**下面的点值接口与分支已证明；真实 R792 尚未返回，所有新点运算仍待公开 Actions。**

本接口消费 [R804](../results/R804-original-selected-map-reuse-in-integral-cyclic-module.md)
已经证明的同一八节点链。保持原 $f=f_4$、$c_0,c_1$、
$L=\mathbb Q(b,\zeta)$、$C_b:y^2=x^3+b$ 与原同源 $v$。
它不需要 R803 的全局 $M_6$ 坐标，也不消费或重算五份 Laurent 系数。
已知输入必须是真实成功 R792 的 $\beta_C=f(c_1)$，不能用“待求”字段、
辅助有限域点或任意共轭点代替。

## 1. 最小原来源链

保留四组原 producer，每组均有原 run、core receipt、public input、
certificate、full manifest 与逐项 bytes/SHA：

| 组 | 直接数学输入 | 用途 |
|---|---|---|
| R792 | 最终证书、阶段 manifest、真实 point stage | 原 $\beta_C$ 与已经认证的原实下降像 |
| R735 | 原 CM model certificate | 原 $b$ 的七次最小多项式，绝不改成 $B=\lambda b$ |
| R791 | 原 Hom/Galois stage、原 real-descent stage | 原 $\sigma(b),\rho$、$\rho_0,\ldots,\rho_7$、完整 $T$ 相位及原 $v^\dagger v$ 来源 |
| R794 | 原 selected stage | 同一五个实际映射的整数 $a(T)$、原 Hom 列与原次数 |

R791 的已成 `R791-original-Hom-Galois-matrices.json.gz` 已直接保存
`field_rho`、`field_sigma_b`、`rho_iterates_zero_through_seven`。
其配置逐 SHA 绑定原 R754 gamma descent；这些字段与原 R754 完整下降完全相同。
因此无需下载或重新执行 R754 的 280 维下降、period 或 Weil pairing 数据。
只复用冻结 SHA
`f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251`
的 R754 脚本中原 `QKField`、`Composer` 编码与域运算类；首次新点算术只在 Actions。

R792 的成功输入 bundle 传递 R735；R794 的已成 bundle 传递 R791。
消费者必须同时核 R792 与 R794 对同一个 R791 的 source/run/core/manifest/certificate 身份。
新的一日 bundle 只保这四组所需文件；不保未用旧 q 行、Hodge 三积或其它 producer。
R792 尚未成功时，run/artifact/manifest/point SHA 均只能明确为 pending，不能激活请求。

## 2. 原 Galois 运输作用在完整点上

令 $\rho=\sigma(r)/r$、$\rho_j=\prod_{k=0}^{j-1}\sigma^k(\rho)$。
这些 $\rho_j$ 读原 R791 已成字段，不重新生成下降表。
对任意 $P\in C_b(L)$，定义
$$
T^j(P)=D_{\rho_j^{-1}}\sigma^j(P).
\tag{804P.1}
$$
有限点上的准确式为
$$
(x,y)\longmapsto
\left(\rho_j^{-2}\sigma^j(x),\rho_j^{-3}\sigma^j(y)\right),
\qquad T^j(O)=O.
\tag{804P.2}
$$
原 $\rho_j^6=\sigma^j(b)/b$ 保证输出仍在同一 $C_b$。
这里 $\sigma$ 作用于整个原 $L$ 元素，固定 $\zeta$ 而不固定 $b$。
不能只运输标签或外层有理系数。

因原 $c_1$ 在 $\mathbb Q$ 上，(804P.1)正是 $(T^j f)(c_1)$。
原 $\sigma^7=1$、$\rho_7=\zeta^2$ 给
$$
T^7(P)=[\zeta^2]P,\qquad T^{21}(P)=P.
\tag{804P.3}
$$
原 $T^7$ 绝不能被置为恒等。点值任务可用已成 $\rho_7$ 和新输入点
检查第一式，但某个特殊点偶然满足更多关系不改变原 Hom 的21阶作用。

## 3. 特化后必须用实际点选择群律分支

全局 R804 的 Hom 字用来判定两个**映射**是否相等。
特化到 $c_1$ 后，不同的非零映射可能给同一点、相反点或 $O$。
因此这个消费者的加法分支必须比较实际点坐标；不能用 Hom 字不同来宣称
实际割线分母非零。两个标签各自保留，功能不同。

用射影无穷远点 $O=[0:1:0]$ 和有限点 $[x:y:1]$ 表示全部点。
它们满足原 $Y^2Z=X^3+bZ^3$。
取负和 CM 单位分别为
$$
-(x,y)=(x,-y),\qquad [\zeta](x,y)=(\zeta x,y),
\tag{804P.4}
$$
并固定 $O$。

完整加法按以下互斥分支实现：

1. $P=O$ 或 $Q=O$ 时直接返回另一点。
2. 两有限点 $P=(x_1,y_1)$、$Q=(x_2,y_2)$ 满足 $x_1=x_2$、
   $y_1=-y_2$ 时返回 $O$。这包括 $P=Q$ 为二挠点、即 $y_1=0$。
3. $x_1=x_2$ 且未落入第二支时，曲线方程给 $y_1=y_2\ne0$，
   取准确切线斜率 $m=3x_1^2/(2y_1)$。
4. $x_1\ne x_2$ 时取 $m=(y_2-y_1)/(x_2-x_1)$。

第三、四支统一返回
$$
x_3=m^2-x_1-x_2,\qquad y_3=m(x_1-x_3)-y_1.
\tag{804P.5}
$$
每次真正除法的分母都已由所选分支准确证为非零。
这是原椭圆射影群律的完整分支实现，覆盖零点、二挠点、$x=0$ 和无穷远点，
不以未约分函数表达式在特殊点代入所得的 $0/0$ 代替点值。
每个节点都准确验证原椭圆方程。

## 4. 同一个八节点链及原整数 Hom 字核验

节点同时保存一个实际点和一个准确整数 Hom 字。
Hom 字使用原
$$
E=\mathbb Q[T]/\Phi_{21}(T),\qquad \zeta=T^{14},\quad \zeta^2=T^7,
\tag{804P.6}
$$
在 $1,T,\ldots,T^{11}$ 中的十二个整数系数。
这些约化是新短链标签的准确核验，不重新求旧 Hom 矩阵或次数 Gram。
最终字逐项等于 R794 的已成 `a_in_Q_T_mod_Phi21`，
由原 R794 的完整十二 Hom 坐标见证识别同一个实际映射。
输出保留原 `original_Hom_integer_column`，而不另选 Hom 基。

八个加法节点为：

| 结果 | 具体链 | 加法数 |
|---|---|---:|
| candidate0 | $-T\beta_C+T^6\beta_C$ | 1 |
| candidate3 | $-T^2\beta_C+\zeta^2\beta_C-\zeta^2T\beta_C-\zeta^2T^4\beta_C$ | 3 |
| candidate1 | 先 $P=\beta_C-\zeta T^2\beta_C$，再 $Q=\zeta^2P+TP$，最后 $T^2Q$ | 2 |
| candidate21 | $-T\beta_C-\zeta T^6\beta_C$ | 1 |
| candidate15 | $\beta_C+\mathrm{candidate0}$ | 1 |

原 $\sigma$ 在 $K$ 上固定，故 $T$ 与 CM 单位交换；(804P.1)给中间点的真实运输。
按 §3 处理实际点碰撞，不因为某个加法返回 $O$ 就改变其非零 Hom 字。
五个最终点顺序固定为 $0,3,1,21,15$，原次数固定为
$1485,1521,1602,1674,1728$，均直接取原已认证字段。
它们是原 $g(c_1)$，没有重新平移 $c_0$。

## 5. 真正的 $v\beta$ 与同源核边界

R791 已证原实下降
$$
f_R=f+c(f)=[1-\zeta^2]f,
\qquad q_R=vq.
\tag{804P.7}
$$
因此原
$$
q_R([c_1-c_0])=v\beta=[1-\zeta^2]\beta_C
\tag{804P.8}
$$
在 $B=\operatorname{Res}_{\mathbb Q(b)/\mathbb Q}C_b$ 的原模型中，由原 R792
`real_descent_image`（无穷远支）或 `x_real_descent_Fb,y_real_descent_Fb`
（有限支）给出。有限坐标必须在原 $\mathbb Q(b)$，不是把一个共轭嵌入重新称为原点。

消费者另外用 §3 的完整群律检查
$\beta_C-[\zeta^2]\beta_C$ 与这份真实 R792 实下降点相同。
这一项是独立的原同源像一致性检查，不计入五个所选映射的八个加法节点。
在 $x=0$ 或 $O$ 上也用完整群律，绝不强代含 $y^2-b$ 分母的仿射三同源式。

保留原 R791 的 $\kappa v^\dagger v$ 来源与实际 $v$。
不能将模型上的 $v\beta$ 说成恢复了抽象 $A$ 中唯一的 $\beta$：
同源的有限核前像没有由这个任务求出。
点值完成也不推出任何全局极除子、$\eta$、刚性化比较或高度已完成。

## 6. 可续接的输出边界

输入点核验、原共轭点、每个新增加法节点、五个最终点及同源像核验分别落完整 stage。
每项绑定原 producer、core、R804 proof、此接口、原 field helper 和原 $b$ 多项式。
同标签完整节点只读复用；预算中断保留最后完整节点。
最终证书分别记录：五个点已准确计算、五个 Hom 字已准确匹配、
原 $v\beta$ 已核一致、所有特殊点分支完整处理。
`original_A_coordinate_lift_computed`、`global_polar_divisors_computed`、
`eta_values_computed`、`heights_computed` 均保持 false。
所有可重算大坐标只在一日活跃 artifact 中传给直接后继，Git 只登记脚本、
参数、run、SHA及可证明结论。


## 7. 同一原点的两个真实来源入口

本消费者的逻辑组名 R792 表示原 beta 点输入，不固定其只有一种上游
关系 producer。现支持下列两个实际成功结果；每种均逐原 manifest、
run/core receipt、certificate、点 stage 的 bytes/SHA 与配置核验。

| 上游实际 RESULT | 固定 core SHA256 | 证书点字段 | stage manifest |
|---|---|---|---|
| R792-original-beta-composition | 7b7a5483e560f2d244092af486c8aed606b18c1f3557dddb3b850a290b4e343d | point_spec | R792-stage-manifest.json.gz |
| R792-original-beta-from-R824-relation | a8a33d32b19525896a137fcf02c3fbf07ced88207839e9c89f16c9c527e827bf | point_stage | R792-R824-stage-manifest.json.gz |

第二入口只接受已经准确算出原 beta_C 与实下降像的成功证书，
另外核 original_y_ratio_preserved=true、
synthetic_R787_producer_or_relation_file_created=false 和
original_R824_denominator_and_content_reinserted=false。
其原 y 的真实性由 R824 的已成准确关系及
R824-original-exact-relation-adapter-to-beta-consumers.md 给出。
两个输入具有相同的原 b/sigma/rho、原 f4、c0/c1、点编码与 vbeta 意义；
故第 2–5 节的全部群律、八节点、原 Hom 字及同源像检验逐字不变。

输入配置保留实际上游 RESULT、core、run、source、manifest 和
certificate，输出数学配置另明记 actual_beta_input_result 与
actual_beta_input_point_field。不得将第二入口重标成第一个 producer，
也不得为让旧字段可读而制造一份假 R787 关系或旧 R792 证书。

活跃输入 carrier 同样按真实类型选择：
第一入口为 R792-retained-producer-inputs.tar.gz，
其中旧组为 R735/R775/R786/R787/R790/R791；
第二入口为 R792-R824-retained-producer-inputs.tar.gz，
其中原关系组改为真实 R824，其余五组不变。
R804 仍只从该 carrier 取 R735 model，从原 R794 carrier 取完整
R791 Hom/实下降来源，随后保留自己的最小四组续算 bundle。
carrier 的组名、parent-child 身份和全部实际保留成员 SHA 都核对；
不同规范的原曲线点不能混入这个入口。

两种点来源任一尚未完成时，对应请求保持 pending。
这次适配只扩大准确来源读取，既不计算任何旧 beta，也不改变未执行的
八节点算法、特殊点分支、原 v/kappa 或同源有限核边界。
