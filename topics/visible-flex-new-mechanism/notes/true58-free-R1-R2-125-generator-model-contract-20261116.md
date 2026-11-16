# 真正58自由R1/R2：125生成列与曲率minimax模型合同

2026-11-16。本文为[新模块](../scripts/frame_metric_current168_free_R1_R2.py)的纸面合同；没有执行几何、原函数、参数Jacobian、求解器、编译或测试。

**新问题。** [已闭19变量任务](true58-joint-alpha-R2-status8-no-candidate-20261116.md)只允许 $x=\alpha x_\star$，返回status 8且无候选。该返回不构成整射线或完整控制族的严格不可行证明。新任务释放全部17个R1方向，另保17个R2方向，从原58零增量开始最小化共同曲率上界。冻结祖账为2902.366570826科学秒、147个full values；它们不装入新counter。

## 1. 真实场与新控制

唯一基点、原168场和172盒见[实际接受58](true57-nonlinear168-original-two-grid-accepted58-20261116.md)。取[R514](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)的完整原三样条组合，固定R0增量为零，令

$$
\Delta u=R_1A_x+R_2A_y,\qquad
\Delta v=R_1D_x+R_2D_y,\qquad x,y\in\mathbb R^{17}.
$$

原单Q、全部height和新增九坐标保持实际58的背景值。原三样条按全区延拓使用，不在末片截断。58的metric峰在 $s=.4725,\theta=0$，位于三样条首支持 $.36$之后；所以没有全族固定该峰的源码障碍，但也没有先验下降结论。

固定 $s=\sigma$，原角方向为 $(\alpha_j,\beta_j)$。令

$$
Z_j=T_u\alpha_j+T_v\beta_j,\qquad V_j=a\Pi Z_j.
$$

完整有限恒等为

$$
U=U_0+Vx,\qquad Z_{12}=Z_{12,0}+Zx,
$$

$$
Z_{11}=Z_{11,0}+Lx+H(x,x)+Vy,
\tag{1}
$$

其中 $Z_{11}=X_{ss}$、$Z_{12}=X_{s\theta}/a$、$Z_{22}=X_{\theta\theta}/a^2$。本圈的 $T,Z_{22},X$固定，第一形式、法向、mirror及形算子随 $x$变化。式(1)是[R516](../results/R516-common-first-radial-jet-quartic-domain-and-original-box-curvature-separation.md)的准确有限二次式，不是截断Taylor近似。

## 2. 已付输入和真正新增量

[原R1源码](../scripts/frame_metric_current168_reflected_R1_ray.py)的完整MODEL实际保存了scalar_fields、scalar_frame、原u9/v8、tangent_columns17、primitive_tangent_columns17和V17。新模块直接恢复这些数据及原ring MODEL中的五个位置一/二jets、实际G、两原角网和精确三jet映射。

$a,a_s$字面读取58 CACHE2的selected径向数组。原[exporter](../scripts/frame_complete_body_extension168_selected_cache.py)明确保存metric_a、metric_a_s、metric_a_ss。只取原径向id141；缺失则退出，不调用metric补算，也不从旧ray反解。

因此输入部分有0新ordinary、0新scalar frame、0旧几何J、0旧V17原函数。下面真正缺失的二阶偏导、完整新Pi列及新模型评价均在本次科学钟计费。

原frame偏导在已付当前u/v/theta上为

$$
T_{uu}=-cH,\quad T_{uv}=vc^3N,\quad
T_{vv}=(2v^2-1)c^5H-3vc^5e_3,\quad c=(1+v^2)^{-1/2}.
$$

完整二次项为

$$
H(x,x)=a\Pi[T_{uu}A_x^2+2T_{uv}A_xD_x+T_{vv}D_x^2].
\tag{2}
$$

原angular_basis的u前八列与v八列相同。记为 $b_i$，u第九列为 $r$；写 $A_x=\sum p_ib_i+qr,\ D_x=\sum d_ib_i$。式(2)准确压成：

| 部分 | Pi输入列 | 数目 | 收缩系数 |
|---|---|---:|---|
| uu | $T_{uu}a_i a_j,\ i\le j\le9$ | 45 | 对角 $x_i^2$；非对角 $2x_ix_j$ |
| uv共同八列 | $2T_{uv}b_ib_j,\ i\le j\le8$ | 36 | 对角 $p_id_i$；非对角 $p_id_j+p_jd_i$ |
| uv的core项 | $2T_{uv}rb_i$ | 8 | $qd_i$ |
| vv | $T_{vv}b_ib_j,\ i\le j\le8$ | 36 | 对角 $d_i^2$；非对角 $2d_id_j$ |

125是生成列数，不是rank结论；没有角基拟合或秩执行。不同T偏导的列不跨类合并。已付 $H(x_\star,x_\star)$不能恢复此完整映射。

线性列是

$$
L_j=2a_s\,\underbrace{\Pi Z_j}_{\text{已付}}+
2a\Pi[(T_{uu}u_s+T_{uv}v_s)\alpha_j+
      (T_{uv}u_s+T_{vv}v_s)\beta_j].
\tag{3}
$$

式(3)中括号由paid scalar_frame的Ts_value_part直接取得。每网将真正缺失的17列与125个二次列拼为一个 $(1,n_\theta,3,142)$数组，只调用一次原periodic_operator。两网合计两批、490752个输出binary64；不再计算旧17个V原函数。

实际Pi输入、输出、使用的L17/H125及新局部二阶偏导完整保原stdout。部分失败只保真正完成的数组，不补零或重建。数学线性重组不被称为旧ray浮点逐位等同；新模型有新定义和数组身份。

## 3. 34个物理尺度坐标

令已付三jet矩阵的行是 $\nu_0,\nu_1,\nu_2$。每个模式的三个原物理增量 $c_j$满足 $\nu_0\cdot c_j=0$。选 $p$为 $|\nu_{0,p}|$最大的非零项，同值取先出现者；另外两索引为 $f_1,f_2$。定义

$$
c_{j,f_1}=z_{2j}/4,\quad c_{j,f_2}=z_{2j+1}/4,\quad
c_{j,p}=-\frac{\nu_{0,f_1}c_{j,f_1}+\nu_{0,f_2}c_{j,f_2}}{\nu_{0,p}},
\tag{4}
$$

$$
x_j=\nu_1\cdot c_j,\qquad y_j=\nu_2\cdot c_j.
$$

这完整覆盖原二维物理平面，不丢R1/R2方向。只读已付矩阵，不重算原逆、旧rank或三jet恒等。原172盒全部保留，零宽原盒行仍作为约束。范数为

$$
h\ge4\|\Delta q_{\rm physical172}\|_\infty,\qquad0\le h\le h_{\max}.
$$

$h_{\max}$沿用原盒的充分上界，不暗加旧 $1/128$。callback用固定一次舍入的映射矩阵；最终候选则从真实raw z的精确binary64有理数出发，按(4)准确解码、与原58共同合成、最后一次舍入。浮点callback的x/y与准确解码差异单列。R0准确恒等仅授未舍入的增量，最终binary64候选仍须原门。

## 4. 36变量目标与实际G完整谱门

后端为 $(z_{34},K,h)$，目标

$$
\min K+10^{-6}h,\qquad1000/61\le K\le58.
$$

准确下界仍为1000/61；后端K bound及对应线性行统一采用不低于该有理数的最小binary64，另存其准确binary64值，避免最近舍入值偏低而被最终准确区间拒绝。

唯一初点为原58零增量、K58、h0。首次新多项式评价仍收费，未执行前不把其新浮点残差预写为零。

metric预算为原58的 $.26600541463999305$，两门为

$$
\varepsilon(1+\varepsilon-E)-F^2\ge0,\qquad
\varepsilon(E-1+\varepsilon)-F^2\ge0.
$$

实际G按原paid值保留，不置1。令

$$
w=U\times T,\quad Q=w^2,\quad
p=w\cdot Z_{11},\ r=w\cdot Z_{12},\ c=w\cdot Z_{22},
$$

$$
a=G^2p-2GFr+F^2c,\quad b=Gr-Fc,\quad
t=a+cQ,\quad R=K^2G^2Q^2+ac-b^2.
$$

完整[R525](../results/R525-one-parameter-common-R1-R2-curvature-fibers-and-polynomial-original-box-domain.md)谱门为

$$
4K^2G^2Q^3-t^2\ge0,\quad R\ge0,\quad
R^2-K^2G^2Qt^2\ge0.
$$

R非负不能删除。另保 $Q\ge G(1-\varepsilon)$，明确要求其已付G满足 $G\ge\varepsilon$。全部角点和两网使用同一组控制与K。

解析Jacobian由式(1)和125个二次系数直接微分，每次仅收缩新列，不重新FFT。新增K列为

$$
(8KG^2Q^3,\ 2KG^2Q^2,\
4KRG^2Q^2-2KG^2Qt^2).
$$

固定行尺度只在唯一已计费初点评价设置一次，不随迭代变化。整个有限模型仍是浮点模型；最终独立检查原单位未平方四PSD、直接metric和准确原盒。线性norm epigraph保原LP_ROW_TOLERANCE；另外如实报告准确ideal_h≤raw_h是否成立，不把容差通过写成该准确不等式。准确候选hmax门另独立保留。

## 5. 费用、失败与后继真实门

新总600秒含imports、输入、二阶偏导、Pi、求解、输出和失败。一次SLSQP调用180秒、maxiter200、至多600个不同字面输入的完整值+解析Jac。重复输入消费当前进程cache；各类callback与真实失败计数分别记录。使用ftol1e-9、disp false，无重启和隐含内层旧LP。

后端raw36及全部实际返回字段先存再筛选；QP乘子不是严格非线性证书。只有真实success/status0且原单位筛选合格才交候选。即使K仍高于1000/61，也可成为后继有限候选，不能据此授主reach。

候选再由完整body非线性预测、原cfg曲率门、严格eta下降至少1e-7、原14门与准确172盒决定actual。没有资格就0预测、0actual。环模型不替代中段或全body门。

MODEL保新增Pi与映射，NONLINEAR_RESULT保原返回，SOLVE_TRACE保全部实际评价/迭代记录、行尺度、首次与最后/partial原值和Jac。未输出的其它中间cache不声称未来免费可恢复。权威科学末钟在大输出之后采样。

