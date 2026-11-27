# R1124：原 full47 两个特殊 CM 圆盘完整关闭

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：已证明，公开 QC 精确计算成功。**
原 $X_{\rm ns}^+(47)$ 在 $q=4513$ 的标签0、141两个完整圆盘，
其原 $Z_A,Z_B$ 高度方程的共同零各只有相应的有理 CM 点。
结合 [R1122](R1122-certified-original-six-complete-CM-disks.md)，
全部八个原候选 CM 圆盘的内部唯一性已付清。

本篇只新读这两个盘。
六盘的完整结果、共同高度、Jacobi 坐标和原第三类值没有重算。
全局标签转移及一般素数问题分别沿其原来源接续。

## 1. 实际执行及来源

- source：[b0ffe03ad95291999ef104b217cd30b3cdbad93a](https://github.com/Rogerhu12/math-research-public/commit/b0ffe03ad95291999ef104b217cd30b3cdbad93a)。
- [run46000409994](https://github.com/Rogerhu12/math-research-public/actions/runs/46000409994)，
  [job140510309243](https://github.com/Rogerhu12/math-research-public/actions/runs/46000409994/job/140510309243)，attempt1。
  checkout、固定镜像、数学步骤与整个 job 全部 success。
- 数学耗时 **117.687072366秒**，预算2400秒、reserve60；
  固定 SageMath10.6 官方镜像与 python-flint0.9.0。
- 完整 receipt 的 status=complete，requested_CM_disks准确为[0,141]，
  all_requested_disks_unique=true。
  root/global独立读取实际完整日志；
  root再核完整 completed 的 canonical SHA、source及请求 pin。

新的薄入口只消费旧六盘共同请求的不可变完整 SHA，
明确替换圆盘集合、四条已成第三类记录和本次自己的 C 证书。
父进程与 fresh flint 子进程均核新请求、旧共同请求和全部来源。
原数学消费者和旧六盘文件没有修改。

## 2. 两个实际原矩阵

沿 [R1103](R1103-original-CM-tangents-finite-field-third-kind-and-QC-first-jets.md)
及 R1122 的同一规范，设
$$
P_0=B_qu_{-4},\quad
L=[\lambda_0,H\lambda_0,\ldots,H^{72}\lambda_0],\quad
\lambda_0=q^{-1}\log P_0,\quad H=T_3+T_5,
$$
$$
K=\kappa/a,\qquad a=(T_2-1)/2,\qquad b_y=L^{-1}e_y.
$$
原 $c_{-4}=B_q^{-1}$，八个 $c_y$ 均消费 R1120 的
真实带符号 Jacobi 坐标及既有整 Hecke 关系。
原 fixed-cycle 函数及其 $1/2,2/3,1/23$ 不变：
$$
d_{Z,y}=\frac{\frac12F_4(Z)c_{-4}+\frac23F_3(Z)c_{-3}-2Zc_y}{23}.
$$
实际首层为
$$
A_{Z,y}=-\operatorname{Tr}(KZb_y^2),\qquad
B_{Z,y}=\operatorname{Tr}(Kb_yd_{Z,y})-\alpha_{Z,y}.
$$
每条 trace 使用全部73方向；$\alpha$ 取 R1123 的本除子、本目标值，
已除六，不再重复清分母。

以下数值都在 $\mathbf F_{4513}$ 中，行次序 $Z_A,Z_B$，
列次序 $A,B$：

| 标签 | $j_{\rm CM}$ | $A_A$ | $B_A$ | $A_B$ | $B_B$ | 行列式 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 508 | 508 | 3609 | 2277 | 294 |
| 141 | 1728 | 2745 | 1547 | 7 | 3142 | 3157 |

供核对局部减项的完整线性读数为：

| case | 原全局线性项 | 原局部 $\alpha$ | 相减后的 $B$ |
|---|---:|---:|---:|
| 0/$Z_A$ | 1039 | 531 | 508 |
| 0/$Z_B$ | 4134 | 1857 | 2277 |
| 141/$Z_A$ | 3330 | 1783 | 1547 |
| 141/$Z_B$ | 3671 | 529 | 3142 |

两个实际矩阵都 rank2。
receipt逐盘给 common_reduction_polynomial=[0,1]、
common_roots=[[0,1]]、some_linear_coefficient_is_a_unit=true。
不是由六个一般盘外推特殊点行为。

## 3. 为什么覆盖完整特殊圆盘

原整 coarse 参数严格是
$$
z=j-j_{\rm CM}=4513t,\qquad t\in\mathbf Z_{4513},
$$
不是特殊点的栈参数。
R1103已证明原 restricted-analytic 函数在**整个**此圆盘的整尾，
且两约化准确为
$$
t(B_{A,y}+A_{A,y}t),\qquad t(B_{B,y}+A_{B,y}t).
$$
非4513项使用 R1103 §6.1 的全原整 Poincaré 刚化，
坏47项使用 R1074 的整个 tube 来源，保持所有标量和二次扭转。

实际两个矩阵的非零行列式给共同 gcd恰为 $t$；
程序另外实际核 gcd 与全部根。
因此任何共同整零都先满足 $t\equiv0\pmod{4513}$。
又有一个原函数的一阶系数 $B$ 为单位，
其在这个剩余类中的零唯一。
原有理 CM 点 $t=0$ 满足全部原高度关系，所以唯一零就是它本身。

由此排除的是整个原4513盘中的其它有理点，
不是一个未明确半径的更深邻域；
也没有把 $t^2$ 的重根当成唯一性。

## 4. 共同原格与完整矩阵桥

全部共同输入重新读入时逐项核旧哈希，准确保持：

| 对象 | 本次核准值或 SHA-256 |
|---|---|
| $\det L$ | 4475 |
| 完整原 $L$ | 6b0537de198a5431b0eb0d7c4907155d54ef643422b5c5b27142db203dc6d618 |
| 完整原 $K=\kappa/a$ | 48842ecac11d0b32163b3c4ba97c208aac71a3d8c56d1637fac94cd25bdb7ff0 |
| 全部八个原 CM 坐标 | 6e4b18e32a99bfcd38d265bb66e3947e23537e036d0304ff9d3861a5f37f12e1 |
| 原完整 Cartier row matrix | deda5ed6dbe8122f243c46bb60245cf8facc00b6040a8f34958c9ca4241d855d |

消费者在接受四个局部值之前，核完整
$C_{\rm row}=1-B_q(H)$ 的矩阵 SHA，
不是仅核谱或 determinant。
原高度Norm$(K)=2992$、整高度 determinant3972、
73个 moments、trace Gram、$\kappa$ 与 resolvent 的旧 pin 也全部通过。

## 5. 复现 pin

| 对象 | SHA-256 |
|---|---|
| 两特殊盘薄入口 | 44a340495dd2dc54f3da006509b5dcd1e1529dd06fb5cd72c4473c95af45e63b |
| 两特殊盘方法 | f0e81a4662a5204a5127bc5b9b9a647ebe89dc6617bfb58dd0732d74ea5e630e |
| 两特殊盘实际请求 | 1558656f49c800cc16669d11bc755b205275d39dea1c5e429cafcb29a15ccd8a |
| 不可变六盘共同请求 | 95e8ccb0bd7906f1c0c47fbebc794c77994b3fd5cba58766d31fbc53ac3dbc0b |
| 完整 completed 结果 | 23f2137019e4a98e2d0fb1976872d4233cba6f4e34e165d830167b1de6cd70cb |
| 完整 QC_first_rows 子证书 | 3fa8bf6011906c191473f3060a833a9fcdac5691b6245043ef2880c351f6c4ad |
| 消费的四个新局部值 | 1056547ddb3efa107b5a01dc9fa093c06589dd1f27803897e6913ef3d5438eab |
| 消费的新完整 C 证书 | 8d2b552051d6b8b62ccffc24c5bef8e276ceb9e9c388fb4da4fc7fb193006856 |

入口：
[方法](../notes/2026-11-27-full-p47-QC-special-two-method.md)、
[请求](../notes/full-p47-QC-special-two-request.json)、
[薄入口](../scripts/full_p47_QC_special_two.py)。
第三类值来源见
[R1123](R1123-certified-original-four-special-CM-Cartier-values.md)；
原全73高度与带符号坐标分别见 R1102、R1120。
只保源、小输入、小结论与run/job/hash，无raw或artifact。

## 6. 立即接续

R1074/R1086的全标签转移现在可与
R1122、R1124的八个完整盘内部唯一性接合。
该全局范围逐条沿原来源审核，另登记固定47分类。
本篇没有据有限素数结果终止一般素数的主目标；
绝对常数或真正无界反例族仍须继续。
