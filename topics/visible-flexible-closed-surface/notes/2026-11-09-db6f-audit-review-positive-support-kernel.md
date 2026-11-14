# 独审：两个保留点对全域正径向支持的上界

审查者：/root/independent_geometry，2026-11-09。结论：**PASS**，范围为 root 的短证明、固定两点身份、纯 Fraction 脚本及其单次完整独立重放。它排除指定全域支持门，不排除同一固定片通过其他方法获得足够 reach。

我此前写了作为输入的 Poisson 模型和径向投影分离补充，但没有参与本次换中心两点上界的完整证明或 root 脚本实现。本审稿没有改写任何作者文件，没有求解或读取当前 M15 优化态。

## 1. 冻结审查对象

- notes/2026-11-09-db6f-root-positive-support-kernel-obstruction.md，4616 B，SHA-256 0b3ad1fcdf31af4653547ae5d9d2bba520096210887f5ff24adf4f1ed7a2531f。
- scripts/db6f-root-positive-support-kernel-obstruction.py，3378 B，SHA-256 56ae6c786589dfdbf9ed0acb4dcf7e1d0a9a17ee444f309e0c761e17623582cc。
- notes/2026-11-09-db6f-root-positive-support-kernel-obstruction.json，2054 B，SHA-256 eb163aacdf57abb4511838753a3effec7b582ddc8ee27f9f3120d65483bc38c4。

作者证明 §§1–4 和全部脚本已逐项阅读。另独立从 R27 原始标量区间重建平方根与向量中心，未导入作者程序。

## 2. 换中心覆盖论证

对紧、连通、无边界的 $C^1$ 嵌入曲面及连续单位法向，若
$x\cdot N(x)\ge\sigma>0$，则任意 $|b|<\sigma$ 都满足
$(x-b)\cdot N(x)>0$。特别地 $b\notin S$，径向投影的微分在切平面上可逆。

因此径向投影是局部微分同胚。紧性使其 proper，像开且闭，故覆盖 $S^2$；连通覆盖的目标 $S^2$ 单连通，因而只有一层。证明对曲面原先是否已经声明为球面没有额外要求，覆盖结论本身给出了这一点。它也不需要一个未经证明的“实体星形”假设。

给不同 $p,q\in S$ 和 $0<\lambda<1$，取

$$
b_\lambda=\frac{p-\lambda q}{1-\lambda}.
$$

则
$p-b_\lambda=\lambda(q-b_\lambda)$。两个射线向量非零：否则会推出 $p=q$。如果 $\inf_Sx\cdot N>|b_\lambda|$，前面的投影必须单射，与这两个不同点矛盾。若下确界非正，所需上界本来就平凡。因此作者的

$$
\inf_Sx\cdot N\le |b_\lambda|
$$

对所列全部情形成立。严格和非严格号没有偷换。

## 3. 实际点身份与有理包围

环片点是

$$
p=(-7/20,0,1/10),
$$

它严格位于新固定圆领的径向区间 $[.34,.36]$ 中。另一个点是旧 Poisson 球面小帽的同一轴点

$$
q=(-X,0,Z),\quad
X=H+\frac{H}{5L_b},\quad
Z=\frac3{10}+\frac{31}{1000L_b},\quad
L_b=\sqrt{4H^2+(31/100)^2}.
$$

该点的帽法向就是帽轴，因此属于任何正角半径的小帽。分母中的 $31/100$ 来自原球心高度加实际柱带半高；辅助包围的新高度 $B=.09$ 没有替换它。

$\lambda=1/4$ 代入后，中心分量正确地成为

$$
b_x=(X-7/5)/3,\qquad b_z=(2/5-Z)/3.
$$

脚本对 $H$、$L_b$ 的区间相关性采取独立向外包围，虽然略松但不会漏包。所有分母为正；$b_x$ 的区间全负、$b_z$ 全正，所以各分量平方的最大端值相加确为安全上界。源文件 SHA 已固定，输入并非未验证的显示小数。

## 4. 独立实际重放和不同路径的复算

作者脚本换成新输出路径实际运行完毕：

~~~bash
python topics/visible-flexible-closed-surface/scripts/db6f-root-positive-support-kernel-obstruction.py \
  --out topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-audit-positive-support-kernel-replay.json
~~~

工具 receipt 6ea210，exit 0。新输出与作者报告逐字节相同，SHA 同为 eb163aac…38c4。

另写的 scripts/db6f-audit-positive-support-kernel-check.py 不导入或调用作者函数。它从 R27 原始 case 中相加得到 $H$ 两端，分别用 $[0,4]$ 上 122 次精确有理二分产生 $L_b$ 的端点。所得四个源端点与旧已审报告完全一致。再把帽轴点按“球心加半径乘单位轴”构造，最后执行仿射中心公式，重建五个中心字段和完整平方范数上界，均与作者同值。

该独立检查实际 receipt 2acc6e，exit 0；输出为 notes/2026-11-09-db6f-audit-positive-support-kernel-independent.json，SHA ff5094f0d1102570fb407c8cae08c177ec5113ed6acfa65ba83bb7012124459d。

它还给出一个更粗但容易人工核验的独立证书：

$$
-.039<b_x<-.038,\qquad .029<b_z<.030.
$$

所以

$$
|b_\lambda|^2<
\frac{39^2+30^2}{10^6}
=\frac{2421}{10^6}
<\frac1{400},
$$

最后严格差为 $79/10^6$。这独立确认了
$\inf_Sx\cdot N<1/20<189/2500$，不依赖打印的
$0.002290740689283086$。

## 5. 哪个结论被排除，哪个没有

通过的结论是：同时保留这两个精确点的闭连通曲面，不能具有
$F\cdot N\ge.05$ 的全域下界；因此也不能满足以
$\rho_{\mathrm{goal}}=.0756$ 调用 R10 的那个支持假设。

这**不是 reach 上界**。例如半径为 1、球心距原点 .99 的球面，其外法向支持下界为 .01，而 reach 仍为 1；这只说明二者在一般逻辑上不能倒置，并非为当前保留片构造了一个球面。对当前模型，全点对认证路线仍须单独研究。

c=.35 的无重复原点射线结论也仍然正确。新证明换用了一个非零中心，所以它是更强的必要门，不能据此称旧射线分离计算错误。原局部片支持和保留片法向点对界亦不受影响。

本次没有发现必须修改作者证明或脚本的数学问题。没有把审查 PASS 延伸为任何完整闭等距族、当前 M15 状态或最终完成标准的声明。
