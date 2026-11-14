# 完整第四阶 range 的准确代数编译器

日期：2026-11-14。状态：源码与小型恒等式开发记录；完整编译等待本公开仓库 Actions。本文没有新的 profile 积分、真实几何积分、优化或 ODE 数值结果。

## 1. 目标与固定数据身份

源码为 `scripts/literature_range_profile_algebra.py`。它实现《完整二次 forcing 的分子演算：真实变系数 range 与有限阶闭合》的公式 (2)、(5)、(6)、(7)，保留真实变系数、连接段和全部积分历史，编译固定目标

$$g_\epsilon=g_X+\epsilon^2(dY_f)^2,\qquad q=f+ig$$

的完整第四阶 forcing。输出有限表达式的规模和有序结构 SHA256，不评价任何具体曲线或 profile，也不把某个表达式非零、某组生成元独立当成编译结果。

未来若评价完整四块模型，几何输入必须是 R45 的准确单路径 P：其 frame 由 I 到 $D=\operatorname{diag}(-1,1,-1)$，标量端芽相容，且单 P 的二阶周期算子为零。完整几何是

$$P,P,P^{\rm rev},P^{\rm rev}.$$

旧 R37 的 Klein 八块、N=16384 实例不能作为这个四块输入；其 M、位置闭合和连接记录也不能迁名冒用。当前编译没有提供任何具体 P，亦没有产生新的实体几何。

## 2. 六个基本张量足够重建五个第四谐波

记 $H(U,V)=\mathcal S(U,V)/2$，作普通复双线性延拓，绝不在这里插入复共轭内积。置

$$A=Y_q,\quad B=\mathcal I H(A,A),\quad
U=\mathcal I H(A,B),\quad V=\mathcal I H(A,\bar B).$$

这里 $\mathcal I$ 表示**同一右 collar 锚、同一全局 s 起点、零初值 W 的形式恢复**。只有两条完整 range 已经成立时，它才是周期双 collar 方程的真实右逆。约束外的真实左尾和未闭合的 W 继续保留。

因为 h、k、omega 和这套锚都实，恢复与共轭交换。故 bar B、bar U、bar V 可以共用同一组实系数历史，交换固定 profile 函数 q 与 bar q；不需要重新设置每个 P 或连接段的初值。

令 $\zeta=e^{-i\theta}$，则

$$Y_\theta=(\zeta A+\zeta^{-1}\bar A)/2,$$

$$Z_\theta=((1-\zeta^2)B+(1-\zeta^{-2})\bar B)/4,$$

$$W_\theta=\{\zeta^3U+\zeta(-U-V+\bar V)
+\zeta^{-1}(-\bar U-\bar V+V)+\zeta^{-3}\bar U\}/4.$$

定义六个基本第四张量

$$\mathsf P=H(B,B),\quad\mathsf Q=H(B,\bar B),\quad
\mathsf R=H(A,U),\quad\mathsf S=H(A,V),\quad
\mathsf T=H(A,\bar V),\quad\mathsf J=H(\bar A,U).$$

完整第四 forcing 是 $-H(Z_\theta,Z_\theta)-2H(Y_\theta,W_\theta)$。其 $\zeta^4,\zeta^2,1$ 系数分别为

$$-\mathsf P/16-\mathsf R/4,$$

$$\mathsf P/8+\mathsf Q/8+
(\mathsf R+\mathsf S-\mathsf T-\mathsf J)/4,$$

$$-(\mathsf P+\bar{\mathsf P})/16-\mathsf Q/4+
(\mathsf J+\bar{\mathsf J}+\mathsf T+\bar{\mathsf T}
-\mathsf S-\bar{\mathsf S})/4.$$

另两个系数是相应共轭。源码不只打印这些文字：它实际线性组合各张量的完整 ruling 分子和 characteristic RHS，保存五个谐波的项数与表达式指纹。

一个很小的自由对称双线性 Fourier 计算独立由 $Y,Z,W$ 的定义展开三式，并检查第二、第三场及第四 forcing 在准确种子 $\theta=0$ 为零。另一研究代理已逐项手算核对三式和同锚共轭规则。

## 3. 编译的两种代数

固定 profile 生成元是 xi 的有限次幂、q/bar q 的 jet、这些项的乘积，以及同一右端 r 锚的 Volterra 原函数。原函数求导严格回到被积式；共轭连同原函数一起交换。没有按 packet 切断尾积分。

s 系数用有向无环图记录有理常数、h/k 的真实导数、omega、乘法、加法及实际积分状态。规则始终为

$$\omega_s=k_s/(2h),\qquad (W_a)_s=(\mathcal R_H)_a.$$

新状态的初值只在全局起点设零一次。系数加法保留嵌套 DAG，不反复展开历史；乘法和有理数是准确的。保留了冗余表达式，不据语法上有几项推断数学秩。

源码逐通道检查 profile 振幅齐次阶数。第四阶段只编译 forcing，不提前恢复一个尚未满足两条 range 的第四场。

## 4. Actions 命令、预算与输出

完整编译在命令行入口检查 `GITHUB_ACTIONS=true` 和 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。正式命令为

```sh
python topics/visible-flex-new-mechanism/scripts/literature_range_profile_algebra.py \
  --max-order 4 --progress \
  --max-coefficient-nodes 750000 --max-profile-atoms 100000 \
  --max-separated-terms 100000 --max-seconds 300 \
  --out topics/visible-flex-new-mechanism/notes/full-fourth-profile-algebra.json
```

若到预算，程序写明 `resource_budget_exceeded`、已完成通道和资源状态后以退出码 2 返回；这不构成数学否定。成功的 `complete` 只说明准确形式编译完成。

报告包含源码 SHA、Actions 身份、每通道项数、真实 s 状态数、所需 jet 阶数、五个完整第四谐波、系数 DAG/profile 原函数 DAG/状态 RHS 的有序 SHA。摘要限制为 1 MB；不输出庞大表达式数组或任何几何数据。

本地只运行

```sh
python topics/visible-flex-new-mechanism/scripts/literature_range_profile_algebra.py \
  --toy-only --out topics/visible-flex-new-mechanism/notes/literature-range-profile-algebra-toy-20261114.json
```

它检查小型乘法求导、右锚求导、状态 RHS、共轭及上述自由 Fourier 身份，不建立完整研究目标。

## 5. 开发记录与结论边界

早期原型曾在本地作二、三阶表达式开发检查，留下 `literature-range-profile-algebra-order2-20261114.json` 与 `literature-range-profile-algebra-order3-20261114.json`；另一次朴素四阶全通道重复展开未完成，未产生完整四阶报告。这些仅为源码开发记录，没有评价 profile/几何，亦不作为正式完整编译或数学相容性的证据。之后完整目标统一由上述公开 Actions 执行。

当前编译对应固定第二阶选择及其 canonical 第三场。零二阶周期算子的准确几何上，全部第三 gauge 不改第四 period；第四 ruling 则应落在**同一个全局**三维 w 空间。这个商空间条件仍须用真实同一几何、同一 profile 支付，不能逐段独立选择 gauge。

输出没有证明两条完整第四 range 已成立，没有供给有限族、嵌入性或 reach。下一步是在完整编译上保留真实函数依赖，先用同一全局 profile 设计完整第四条件；任何具体积分与求解继续只用本公开仓库 Actions。
