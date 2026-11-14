# 外题精确闭合路线与本题可见振幅的接口

2026-11-12，visible-exact-astra-f6a2。用户明确授权读取其它文件夹后，
完整阅读 [源 R520](../../continuous-flexibility-swarm/results/R520-actual-newton-zero-height-closed-flexibility.md)。
本记录只说明已经核对的原文结论、输入和本题尚需支付的差额，不宣称已独立
核验它列出的全部上游证明，也不把源题的完成标准换成本题标准。

## 1. 读到的准确结论

源 R520 组织了充分小振幅参数 q 的精确闭合构造：真实当前算子、可数轮
良参数集、完整受迫 Green、非线性 Newton 和 Cartesian 零二 jet 重建。
原文最终得到闭 C² 同度量族和固定帽/标记；它选择 q 足够小，但没有提供
能直接推出本题 held 位移至少 .05D 且全时 reach 至少 .03D 的有限 q 数值。

因此它为本题提供可适配的存在机制，而不是本题现成的可见振幅证书。
把种子乘一个大常数、再声称 q 很小，不能保留原证明常数：源的 profile、
物理几何、全传递、谱隙以及转换费都必须随实际乘积重新支付。

## 2. 不能省略的完整传递

源的对角模型除了主圆周返回角，还有 |j|⁻¹ 和 |j|⁻² 的真实相位修正。
完整目标分母的门为某个正 Γ 下的

\[
 |1+\mathcal D_{n,m}(j)|\ge
 \Gamma_\infty H_m^{.4}\langle j\rangle^{-1.3}.
\]

源模型具体含有主返回平移、完整参考 \(Q_{0,m}\)、两个低阶相位和 mean 通道。
本题 R30–31 的主返回共轭不能自动给出这个分母。逆频率相位在小分母尺度
上仍可能改变可逆性，必须跟着实际当前图计算/约束。

源的余项平滑增益约 1.99，须在同一强域、全频切分及同一受迫源空间里与
1.3 阶分母损失组合。不能只写一个有界的主符号、随后忽略 cap source、
normal shear、反馈方程或像空间的要求。

## 3. 小量和代价为何仍有工作要做

源采用直接对数频率权以及随轮次减少的宽度；宽度费和实际普通源 Green
费进入每一步。参考尺度到实际尺度的初次转换还具有 q 的负幂代价，指数
Λ<1/4；初始源是 q^(2−Λ+o(1))，再由预先固定的代价表选择 q 足够小。

其收敛证明把未来所有代价合进残差门序列，并以嵌套紧良集选到同一个
实际参数。实际 provider 必须先在完整参数域上给出，才能合法筛选；不能
只在最终 Cantor 集上假定光滑参数依赖。逐轮 Whitney 延拓也属于输入。

本题有限幅近似图可走“先付真实当前逆和邻域预算，再用已小残差启动”的
后验版本，但必须给出有限且可比较的常数，不能从源 q→0 的论证直接得出
当前 .06 振幅已经落在允许域内。

## 4. 已取的源文件及阅读范围

以下 SHA256 对提取出的原文计算；原文保留在源题，未复制进本题。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| R520-actual-newton-zero-height-closed-flexibility.md | 70061 | 919f21d91c1e6597e44be0d875d435a9177d925b44e6eec50bf6bedbdbfc292f |
| R513-direct-log-physical-local.md | 97134 | 637cdf810765fa5913065b3618ad4025d9bbbcc6f98fcb49489df21288ffbca9 |
| R517-cumulative-direct-log-m3-high.md | 67563 | f5f3c7254ae283f20a6f783de400f117c032271f0a461fd31adee6a683030ba6 |
| R518-cumulative-current-green-network.md | 44326 | 1aa634f02dea2f4aa6b88a5569f3bd98fa15544e2f0da0a3f3adaaa18c630e13 |
| R519-cumulative-current-green-flux-jets.md | 43894 | 5b79407b01cfb60dc980cf13e816453b28e7799a091a692d26d8467cb121b908 |

root 已读 R520 全文、R517 的开头适用定理/前提及R513 §§0–1、4–6。并行推导者已读 R513
§§4–6、9、12–13，核对真实 cap form、source contact、Cayley、J-polar 和
feedback 结构。R517–519 其余证明尚需按实际使用逐项阅读；表中的源哈希
相合不是那些数学输入对本题成立的证明。

## 5. 正在应用的实际对象

本题 R32 推导对任意星形当前图 F(u)=u/ρ(u) 的完整线性化：
令 B=Hessρ+ρσ，得到球面算子

\[
 D_\rho w=\operatorname{div}(\operatorname{cof}B\nabla w)
              +(\operatorname{tr}B)w.
\]

这不是只取主符号。一次球谐 Y=a·u 满足 DρY=0；在 Y>0 的单个半球帽
内，精确 ground-state 变换

\[
 D_\rho(YU)=Y^{-1}\operatorname{div}
             (Y^2\operatorname{cof}B\nabla U)
\]

把完整零阶项消掉，同时必须变换两迹及受迫源。真实端口应为
U=w/Y、p_U=Yp_w−wp_Y；这样保持通量。Y 在腰部可能过零，不能免费把
这个帽内变换扩展成整个球面的坐标。

后续应逐项比较这个实际散度型帽的转折阶数、normal shear、外部 Robin
最大性、source/contact 和强域与源 R513 的输入。多片固定帽还要求切向
重建的相对 Killing 值为零；全局去掉一次刚体运动不能替代这一条件。


## 6. 固定型别更新的实际残差因子

新增逐项阅读源R492的§§0–1、10及实际主系数/根部段落；root和并行者分别核对。
原文65861B，SHA256
`d444aec2a85260fb392a35e06bd1ba2b58e2b808e1bbec72dac226c9fd77b07c`。
R499已取98562B，SHA256
`954edc7ebab86de15bb5a249981db4070f411f1cdc6295691e6e7b4c79cec2d7`，
并行推导者已按实际使用核对B§§0–9，root另读B§§3–5的完整源/contact与物理角尺度段落；
不是全文或本题适用性已经通过。root另读R517开头至第395行的真实两次同调公式；
R513并行阅读范围也包括§11，未读部分仍不作已核验输入。

R492保留实际a,b，把c改成固定径向型别的值；真正线性化与修正算子的差是
`∂θ(B_F F ∂θ)`，其中F是当前非线性残差。这是含残差因子的Newton修正，
不是把角依赖主项无条件删掉，也不是一条无需估计的实际逆等式。

本题R37已从自己的星形图和目标metric独立推得对应式、真实conormal、
帽ground-state变换、曲率差及应变重建误差。其特征速度需要G_actual，
即使目标metric径向，也不能用G0替换这个当前面积密度。还须支付
同一个修正算子的全传递、普通源和loss，才可进入实际收敛证明。

## 7. 邻题当前状态与新增本题适配

在提交007af8397b91224fbd7128279e35595be3fbb83d的树上，root完整读
visible-flexible-closed-surface的README(4325B，SHA256
`2b9fbc1cf4aa7cf787e125385ecbc2b9df67b2bba325b5dbf38fe10db0fbe934`)
及HANDOFF(8238B，SHA256
`bfd863aecc6dd217ce8d6c2bcac8b965ad2a26aff4b269735a8b10af6fab6182`)。
该题仍进行中。其完成口径容许指定的数值误差与进一步同度规收敛路线，本题则要求
真实精确存在，二者不能混同。其旧flat17 M12连续metric界约2.57212e−8及厚度/可见性
预算有本题R1接口，但不能迁给当前已换mean/profile的phase候选。

其HANDOFF报告R112有非圆pullback线性残差9.72e−10，实际C²场与连续证明尚待补齐；
这里只读取状态文件，未读取R112/R113全文，也未授予其本题全频逆结论。

本题R39–43现已独立写出当前需要的有限Airy全源、真实unitary正常形、直接log变角、
Dyson强余项和单根首逆频率符号。R43使用的Airy振荡首项另对照DLMF9.7.9–12；
显式Volterra误差在本题证明，不把渐近式直接当整个频率轴上的界。

2026-11-12 06:36 UTC，在本次main树be982bd6ec488db1fdf01e4d65d1390cb351b465，
root完整读取continuous-flexibility-swarm当前README和HANDOFF，SHA分别为
216a6d6f6ff3dfcc53604792c9609a7b0737b86aec26a1e8bd4411565ad14b33、
849b2ef0899c29aee58d92d84cf428ee77a142512e620b44068319476c5940ce。
它确认R520已经按该题原A标准完成，并明确“一次固定充分小振幅q”后构造。
这是已读R520的同一适用边界，没有新增本题5%可见性、reach/D或当前候选的
有限幅校正预算。本次只读状态入口，未把其列出的33项正式依赖或两个审查报告
记为本轮已全文读取，也未修改外题。


2026-11-12续：root再次逐项读R499 B§§4–5完整Ai残差/物理源和contact段落；
本题R45独立强化完整内部源接触，R47用固定Fourier lag的L²径向估计支付真实混合坐标，
并明确真实边界B∂与其伴随，未照搬源中的未验证常数。R46的strict负区传播、几何势
有限部及PT校准在本题独立推导；Ai初值和渐近首项另核对DLMF §§9.2、9.7。
