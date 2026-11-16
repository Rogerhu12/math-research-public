# R843：原 p=41 CM 点非挠及原 Hom 值的准确零判

**状态：实际证明完成。** 原第4号整数Hom映射的点
\[
P=f_4(c_1)\in C_b(L),\qquad C_b:y^2=x^3+b,\qquad f_4(c_0)=O
\tag{843.1}
\]
非挠。所用点就是R840/R841绑定的原点；证明没有把任何RR候选当作原坐标。
由原有理primitive点差及其Q简单因子，进一步得到每个非零原L-Hom在该点差上的值非挠。
本结果没有计算原eta或高度。

## 1. 实际有限证书

公开 [run43778335282](https://github.com/Rogerhu12/math-research-public/actions/runs/43778335282)，
compute job133009730596，source a7d3c0f6d4b9c0d10dfd1ad1d07f14fbbd2c2d57。
数学0.8540575309999987秒、59个完成stage；
2026-11-16T00:06:16.241672+00:00正常结束，退出码0、error=null。
core总秒数为0.8545047340000025。

在已经使用的同一辅助素数
\[
\ell=1000000753
\]
选中了原branch0。真实原根为
\((\bar B,\bar s)=(3197390,99932770)\)；
原 \(f_B'(\bar B),2\bar s,\lambda\) 及h0的有理分母均为单位，
其中 \(B=\lambda b,s=1+2\zeta\) 的原换基规范保持不变。
唯一Hensel提升给嵌入 \(L\hookrightarrow\mathbf Q_\ell\)，
没有改用别的模型或另一个局部完成域。

实际约化数据为
\[
\bar b=637573097,\qquad
\bar P=(250197643,437607158),\qquad
\overline{y'_z(P)}=6606439.
\tag{843.2}
\]
b和所需首导均为单位，原h0也是单位。
原模商、原提升根和原h0通过既有恒等式
\[
x(P)=3h_0\,\frac{y(P)^2-b}{y'_z(P)}
\tag{843.3}
\]
给同一P的518位准确局部球。
准确曲线恒等式的来源是原映射；实际球还验证了518位曲线余式含零。

Hasse区间的实际端点为999937509与1000063999。
确定性baby-step/giant-step使用步长356，
命中giant index64与baby index344，得到
\[
m=999960637,\qquad [m]\bar P=O.
\tag{843.4}
\]
这个有限域标量乘已经直接核验。没有声称m是整个群阶或点的准确阶。

在同一个原Qell点上，44个带精度仿射步骤给出了真正的 \([m]P\)。
最后的数据是：

| 数量 | 已确定的真实赋值 | 绝对精度 |
|---|---:|---:|
| x([m]P) | −2 | 515 |
| y([m]P) | −3 | 514 |
| t([m]P)=−x([m]P)/y([m]P) | 1 | 518 |

这里每个球都带实际非零单位部分；例如最后一行准确表示
\(t=\ell u+O(\ell^{518})\)，其中u在模 \(\ell^{517}\) 下为单位。
所以t准确非零，且 \([m]P\) 是非零形式群点。

## 2. 非挠结论的完整理由

**定理843.1。** 式(843.1)的原P非挠。

**证明。** 因 \(\ell>3\) 且b为单位，原模型的判别式 \(-432b^2\) 为单位，
故具有好约化。式(843.4)将 \([m]P\) 放入约化核，
表中 \(v_\ell(t)=1\) 又证明它不等于O。

对于Qell上好约化椭圆曲线，原形式群的单位微分为
\[
\omega=\left(1+\sum_{n\ge1}a_nt^n\right)dt,\quad a_n\in\mathbf Z_\ell.
\]
其形式对数
\[
\log_F(t)=t+\sum_{n\ge2}\frac{a_{n-1}}n t^n
\]
在 \(t\in\ell\mathbf Z_\ell\) 收敛并给群同态。
若 \(v_\ell(t)=r\ge1\)，则每个高次项的赋值至少
\(nr-v_\ell(n)>r\)，因为 \(\ell>2\)。
故 \(\log_F(t)\ne0\)；约化核无挠。
若原P为挠点，则其非零倍数 \([m]P\) 仍为挠点，与上述无挠性矛盾。证毕。

这个证明没有假设 \(\ell\nmid m\)；
它使用真正的Qell嵌入及原好约化模型。
一般分歧局部域的不同形式群阈值没有被移植到这里。
可核作者原文为Milne, *Elliptic Curves*, 第二版II §4–5、Proposition5.4，
[EC2.pdf](https://jmilne.org/math/Books/EC2.pdf)。
Hasse区间的来源为Sutherland
[18.783 Lecture8 §§8.1–8.3](https://math.mit.edu/classes/18.783/2015/LectureNotes8.pdf)；
这里的搜索只求一个消去整数。

## 3. 原primitive有理点与全部非零Hom值

[R616](R616-original-CM-point-difference-and-explicit-height-basis.md)(616.4–5)
给同一个原有理点差
\[
\beta=q_1[c_1-c_0]\in A(\mathbf Q)\otimes\mathbf Q.
\tag{843.5}
\]
[R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md)
(728.24)、(728.32)给这个原primitive因子的真实Q同源模型及
\[
\operatorname{End}_{\mathbf Q}^0(A)=
\mathbf Q(\zeta_n+\zeta_n^{-1}).
\tag{843.6}
\]
右侧是域；由完全可约性，A在Q上简单。
这里没有声称A在L上仍简单，也没有将整个Weil restriction替换为A。

**定理843.2。** 原β非挠；对每个非零
\(u\in\operatorname{Hom}_L^0(A,C_b)\)，\(u(\beta)\)非挠。

**证明。** 原 \(f_4\) 属于这个primitive Hom模块且以c0为O。
若β为挠，其原像P也会为挠，与定理843.1矛盾。

清除q1的同源分母后，取一个非挠 \(n\beta\in A(\mathbf Q)\)。
它的循环群的Zariski闭包是Q定义代数子群；
其单位分量正维，由Q简单性只能为整个A。
因此这个循环群在A中Zariski稠密。
若非零u的值为挠，清除u的分母并再乘一个整数，
所得非零真实同态会消去这个稠密群，从而恒等于零，矛盾。证毕。

对原以c0为O、已运输到同一目标模型的整数Hom映射u,v，
这特别给出
\[
u(\beta)=v(\beta)\iff u=v,\qquad
u(\beta)=-v(\beta)\iff u=-v.
\tag{843.7}
\]
相等关系是原Hom模块中的准确等式。
非零Hom值既不为O也不为二挠；
其仿射y不为零。
对两个非零值，x坐标相同当且仅当对应Hom字互为正负。
因此原点加法的特殊分支现在可以由准确Hom字决定，
无需从模精度“看起来相同”猜测。

这些后果只涉及同一个原点及兼容的真实Hom映射。
它们不选择抽象A上某个未指定同源核原像，
也不许可把任何新映射的平移常数设成零。
原以c0为O的归一化、同靶运输与全部原同源常数必须保留。

R726关于充分大p的旧非挠定理仍独立保留；
本篇用实际数据补出了当前p=41，不借“充分大”涵盖41。

## 4. 精度与来源边界

所有新算术均在该公开Actions运行中进行。
程序消费R841实际carrier中的185件原输入，
直接读取R840的真实518位商、14个原分支、原域参数和R791 h0。
原Dixon、CM评价、RR建议、Hom格和同源常数均不重算。

每个Qell球保存绝对精度及实际已确定赋值。
加减、乘法和求逆分别传播精度；
只有真实非零球才可作分母。
不同整数multiple的x差若仅是零球，就停止为未认证；
只有已知相同multiple才走倍点公式。
本次44个步骤实际都通过，不存在由不确定零选择群律分支的步骤。

没有用未经primitive化的射影Jacobian坐标Z判断形式参数。
最后t的518位精度由带精度的x/y运算导出，
并非在x、y已有负赋值后仍套用一个固定精度标签。
曲线余式含零的检查只作原算术一致性核对，
不替代原映射和原点来源的证明。

## 5. 可复现来源与实际输出

| 项目 | bytes | SHA256 |
|---|---:|---|
| core R792_original_CM_point_padic_nontorsion.py | 25585 | dd3f06a2ed34d31d4d9cc7000eeb5ca763b3fa26b238b418de3e2a47e8dca9c0 |
| wrapper R792_public_original_CM_point_padic_nontorsion.py | 22429 | 5b6bcaa89f690011cc47cfd77463dfd58e526044546d64e3b94203e03f16ef38 |
| source request | 4382 | a3554621a755dadfbe47a71a9f4ac56274defa64f3d68a41c9efde6bc8f5d4b8 |
| 原分裂处方法 | 10785 | b3b88cc94fc3d716bd39227794f3ec780265cd22bdb3082305070e007da0e0a7 |
| final certificate | 6446 | e4f926d374b5225c45036b363f4cc8a0e4918f54a711e2c3e824f803f3a8e506 |
| 原点局部球stage | 14980 | 73b1873adaf88ea6639541479fdd1c681a1f66a13a0d2f17d02a5495d7b7c65b |
| 有限域消去整数stage | 8365 | 6247481dfeca336ca308b3ddb5281540673c17ff3c3df8dd61778beb3272379d |
| 最终非挠witness | 10146 | 62c600cf09063ac5c1e8aff7e73372cf475e51da4c1ca6899542a5222239f6a4 |
| 59阶段manifest | 5398 | bc59d54eed684a825090d4837da804d46218bb125dd5d925d5256735bc8759ae |
| full manifest，67条 | 9787 | 2ed1269af1da10b1b4d18264a2297253eb7d24ecdd6cdb2dee7c4f9324aeb812 |
| 185原件carrier | 1255616 | dd6bb50b4f931fefcf41648946f33f1090bf540e1d9724171d5de8d6a66b86a0 |

实际配置指纹1baa36ebbe6074c172c27cd04e3db78fb1588a904b97731d0ba7410b103ef1d6。
artifact14187431986，名称serre-global-R792-CM-point-padic-nontorsion-43778335282-1，
1903752 bytes、69成员，ZIP SHA256
9adbba8f2826655af7ba37cd14c6c703f6acf81bc9990a9dab459de8cec5f2c3，
到期2026-11-17T00:06:16Z。
本地只完整下载并核了这个1.90MB ZIP、全部69个成员及相关schema，
没有执行新的点乘、Hensel、有限域搜索或局部算术。
机器表格和完整局部球只保在一日artifact，不进入Git。

原坐标的准确展开接受、单值大零证A.1、eta及高度标志仍为false。
非挠后继续消费准确Hom字、R841真点表达式与R842原D空间；
不重复本次44步、搜索或已完成518位输入。
