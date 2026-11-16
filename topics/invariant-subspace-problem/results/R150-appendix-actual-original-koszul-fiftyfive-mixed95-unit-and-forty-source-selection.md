# R150：五十五条原 Koszul 来源的实际混合95单位与四十条原乘积来源选择

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 实际结论

在原固定数域
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336)
$$
的已付合法 place $(127,d-100)$，本次完成同原四次来源核中的混合单位验证：

$$
\boxed{\operatorname{rank}\overline K=55,\quad
\operatorname{rank}[\overline K,\overline T]=95,\quad
\det\overline M_I=69\ne0.}
\tag{1.1}
$$

$K$ 是原十一条二次式的全部55条 Koszul 来源，$T$ 是原二十条三次核来源的全部100条 $u_\ell z_s$。所有原165来源坐标均保留。

按原字典 $j=20\ell+s$，实际选中的四十条原 $T$ 列为

$$
\boxed{J_{40}=\{0,\ldots,33\}\cup\{40,\ldots,44\}\cup\{60\}.}
\tag{1.2}
$$

它们给出原 $E$ 上完全指定的非零混合子式及原伴随坐标公式，落实了
[原 Koszul55 与特征零200/210完整呈示](R150-appendix-original-koszul-fiftyfive-quotient-and-characteristic-zero-twohundredten-presentation.md)
中的原四十列选择。新选择不需要等于此前有限域200呈示的四十条换源列。

本次实际计算全部发生在原合法剩余域，原 $E$ 系数由同一原子式的伴随公式定义；没有把有限域坐标提升为 $E$ 坐标，也没有材料化完整参数200列或证明 Bell 理想为空。

## 2. 同一父对象与完整重建

[原四次核95及特征零270定理](R150-appendix-original-quartic-syzygies-rank95-and-characteristic-zero-twohundredseventy-presentation.md)已付

$$
D:E^{165}\longrightarrow E^{70},\qquad
\operatorname{rank}D=70,\qquad
T:E^{100}\longrightarrow E^{165},\qquad
\operatorname{im}T=\ker D,\quad\operatorname{rank}T=95.
$$

本次旧作业已关闭，未假设其临时文件存活。新 run 43919468897、job 133482555599 按冻结接口真实顺序执行：

1. 重建原十行116来源模型，exit0；
2. 重建已付 high95 父相位，exit0；
3. 执行本混合95 consumer，exit0。

父两个相位的物理与逻辑 SHA、原901字节 manifest、原数学 source 与 semantic binding 均按冻结 pin 实际匹配。父 binding 仍为

~~~text
9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1
~~~

本 consumer 从同一原 $q_g$ 逐重建 $D$ 的全部11550坐标，从同一原二十条 $z_s$ 逐重建 $T$ 的全部16500坐标，且核全部原普通单项式字典、原十一来源标签和全部100列标签。没有调用旧 exact 六逆恢复、有理60阶解或 two-four 解。

## 3. 原 Koszul 字典和实际混合单位

令 $q_0,\ldots,q_{10}\in E[u]_2$ 为原十一条二次最高项。原165行顺序为

$$
(g,m),\qquad 0\le g<11,\quad m\in\operatorname{Mon}_2(u_0,\ldots,u_4),
$$

其中十五个普通二次单项式按原非降指标对顺序排列。对 $a<b$，

$$
k_{ab}=q_a e_b-q_b e_a.
\tag{3.1}
$$

普通对角单项式不另乘2。所有55列在原165行中实际构造，原 $q$ 秩11、$K$ 秩55以及全部3850个 $DK$ 坐标零均通过。

父实际95行投影 $I$ 保持不变。其零基原行号可以紧凑写为

$$
\begin{aligned}
I={}&\{0,\ldots,59\}\cup\{61,\ldots,64\}
 \cup\{66,67,68,70,71,73\}\\
&\cup\{75,\ldots,89\}\cup\{91,92,93,94\}\\
&\cup\{106,107,108,121,122,136\}.
\end{aligned}
\tag{3.2}
$$

这恰为95行。父单位使 $R_I|_{\ker D}$ 为同构。

本次在原 $[K_I,T_I]$ 上按“55条 Koszul 在前、100条原乘积在后”的顺序取主元。前55个主元准确为0至54，后40个主元准确对应(1.2)。因此

$$
M=[\,K,T_{J_{40}}\,],\qquad M_I=R_I M
$$

的实际合法约化行列式为69。

为清楚锁定来源，二十条低来源 $C_s$ 在本篇采用零基 $s=0,\ldots,19$，对应原 commutator 标签

$$
\left(0,\ 1+\lfloor s/5\rfloor,\ s\bmod5\right)
$$

及原种子 ID

$$
\operatorname{id}(s)=10\lfloor s/5\rfloor+1+(s\bmod5).
\tag{3.3}
$$

四十条真实 $W=N_\ell C_s$ 因而为：

| $\ell$ | 原低来源 $s$ | 列数 |
|---:|---|---:|
| 0 | 0至19 | 20 |
| 1 | 0至13 | 14 |
| 2 | 0至4 | 5 |
| 3 | 0 | 1 |

不包含 $\ell=4$ 的原乘积列；这只是实际基选择，不表示这些其余乘积为零。

## 4. 全部原来源坐标完成门

实际计算混合单位逆以及

$$
C=\overline M_I^{-1}
   [\,\overline K_I,\overline T_I\,].
$$

全部门已完成：

| 核验 | 原完整坐标数 | 结果 |
|---|---:|---|
| 从原 $q$ 重建 $D$ | 11550 | 全真 |
| 从原低20来源重建 $T$ | 16500 | 全真 |
| $DK=0$ | 3850 | 全真 |
| 混合95单位的左右逆 | 18050 | 全真 |
| $\overline M C=[\overline K,\overline T]$ | 25575 | 全真 |
| 选中95个混合列的单位坐标 | 9025 | 全真 |
| 选中40个原乘积列的规范坐标 | 3800 | 全真 |

最后一项的顶部55坐标全零、底部40坐标为单位矩阵。全部155条来源均在全部165原行上乘回，不仅验证所选95行。

由原55独立性、原 $\dim_E\ker D=95$ 及实际同原非零混合子式，$(K,T_{J_{40}})$ 是原 $E$ 核基。任一 $v\in\ker D$ 的精确坐标定义为

$$
\binom{\kappa(v)}{\beta(v)}
=M_I^{-1}R_Iv
=\frac{\operatorname{adj}M_I}{\det M_I}R_Iv.
\tag{4.1}
$$

这些是固定 $E$ 常数；没有 $y,w$ 参数分母。实际相位中保存的是有限域完整坐标，不能把它们当成(4.1)的系数数组。

## 5. 原完整来源的回填与呈示

沿父证明，$N_iC_s$ 的真实来源为

$$
\tau_{is}=u_i\sigma_s-\Sigma_iC_s,\qquad
\mathfrak m^T N_iC_s=G^T\tau_{is},
$$

其二次最高来源是 $u_i z_s$。使用(4.1)先减去选中的四十条真实 $\tau_{\ell s}$，再减真正的

$$
G_a e_b-G_b e_a.
$$

最后这些完整 Koszul 来源的原乘回严格为零。减后来源 $u$ 次数至多一，像仍在十正常形中；已付 canonical-source 唯一性使它回到 $B C_{20}$。故本次40个**实际原标签**满足

$$
B\langle C_{20},N_iC_{20}\rangle
=
B\langle C_{20},(N_\ell C_s)_{(\ell,s)\text{ 在§3表中}}\rangle.
\tag{5.1}
$$

加六条 mean 来源，第一轮可用96条梯度列；再加四条保留二字路径作用于六条 mean 和二十条低来源，共24加80条，得到至多200条完整梯度呈示。加十条原 Bell 列则至多210条。

稳定闭包至多两轮完成沿用已付证明；本次不宣称第一轮稳定。新单位验证把原四十列具体化，不把旧有限域数组与新原 $E$ 呈示混成同一个数组。

## 6. 实际执行身份与临时完整相位

执行 source commit 为

~~~text
4f46a8c14212002e9413ed5e6fb0c096a1b8aa8a
~~~

数学 step 为 original-koszul55-mixed95-unit60，实际 child exit0。数学计时为
$0.1269597560000051$ 秒；observer 墙时为 $0.5025294459999969$ 秒，外层墙时为 $0.7156533699999983$ 秒。数学峰值 RSS 为38484 KiB。预算为60秒、512 MiB，observer outer120秒；三种计时没有互相替代。

新数学 binding：

~~~text
b0d3f4b6dfefddccd68f804561d74188c109c151329ac525e2f7b0d2e90a6232
~~~

完整 raw 为9335 B，SHA256：

~~~text
e0ff3b83a46b7bd3c7fd7c81cc36f0eb78c62e48a60d43db52573464135d3c9c
~~~

完成相位为 complete-original-koszul55-mixed95-unit.json.gz：

| 身份 | 字节数 | SHA256 |
|---|---:|---|
| 压缩文件 | 24225 | 4309a9164324c4e7ccf214d25b97c96845feb0e93a0dd0998e6e0a226c5e0841 |
| 完整逻辑 JSON | 86134 | 4214f41007b68fef5ecf152c769030cd1fb850dbd87d350ea49efd5da55885db |

数学矩阵与完整相位只留实际 TMP；完成 job 日志保留回执、来源标签和相位描述符，不把矩阵或相位数组写入 Git。原索引的紧凑规则属于可重现来源参数，不代替矩阵产品。

## 7. 源码、参数及独立日志审计

数学源码为
[原 Koszul55 混合95 consumer](../notes/2026-11-16-r150-original-koszul55-mixed95-source-unit127-789f.py)，
blob 65c4d8a2bcf950c4911044d216faefad0877733b，
16461 B／SHA256 fc1dfea5219a773af1140c3c9e8ba52bcb6acfd36ae67bd325c9317e416d0ab5。

[冻结输入](../notes/2026-11-16-r150-original-koszul55-mixed95-source-unit-inputs-789f.json)
和[完整接口](../notes/2026-11-16-r150-original-koszul55-mixed95-source-unit-interface-789f.md)
保存全部父 pin、同 job 三步重建 CLI 与所有来源门。

根与 normal_annihilator 分别读取已完成 job 133482555599 的完整日志，并实际调用
[独立日志审计程序](../notes/2026-11-16-r150-original-koszul55-mixed95-completed-log-audit-789f.js)。
日志为93880 B，SHA256：

~~~text
83cfc3c9eb8495b7b22e5a4f1fe866d8d73a268f843f30d2c65c51a333012216
~~~

审计逐字重建原165行字典、55个 Koszul 标签、100个乘积标签及40个原来源标签；核 source、runtime、observer 和 semantic binding，并保 Python 数值 token，实际重构9335字节 raw 的完全相同 SHA。

该审计没有再执行矩阵乘回，也没有在 job 结束后读回 phase 数组；完整算术门来自上述冻结生产者的实际执行。重建 manifest 为628 B／SHA256

~~~text
d9211fac3cc3ff06abd00b8ff2b2dec4cb9efc685a6f982027f6a998651054e5
~~~

这一项明确是由完成描述符和冻结 writer 重建，并非审计重新打开物理 manifest。

本篇实际支付同原40列、混合单位和完整场坐标；特征零系数及参数来源由已付原恒等式、(4.1)和(5.1)严格定义。后继仍须独立处理原 Bell 的更高权来源，不能由本篇生成元上界推断单位理想。

## 根的补充复核记录

/root 已全文复核本篇并执行冻结独立审计；[执行身份](../notes/2026-11-16-r150-original-koszul55-mixed95-root-log-audit-execution-789f.json)仅保存源、输入输出SHA及实际范围。根另外重构本次 high95 raw 的8429字节及 SHA256 f57fe3651c77e6ff980fdb671719787ac71a4e9af3c217843be7c951ee20f246，并逐两个完成相位描述符确认与旧实际相位全同。三步实际原门均已读取，未把 job 绿色状态独自作为数学证明。
