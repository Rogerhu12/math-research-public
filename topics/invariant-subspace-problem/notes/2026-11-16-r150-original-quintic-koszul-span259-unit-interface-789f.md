# 原五次 Koszul 来源核与全部300右端：冻结接口及条件呈示证明

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 当前状态与准确对象

本次只计算固定原二次最高项的常数矩阵。这里“五次”指五个 $u$ 变量的普通总次数；对应的低来源二次作用具有 Bell 加权来源权10，不能混作加权五次。

所有来源仍来自原十一条 $G_g=q_g+\ell_g+c_g$、原低20与同原固定数域 $E$。实际计算只在已付合法 place $(127,d-100)$，以同原非零子式认证特征零跨度。rank259 尚未运行，不是预置答案。

若实际满秩门通过，将给完整60列低交换子模的稳定性，并将原梯度／Bell 参数呈示上界进一步降为120／130。若秩未达259，只给该剩余域的完整诊断。

源码已静态冻结；共享执行器不可用，没有本地 AST、编译或数学执行声明。

## 2. 完整原字典

令 $R=E[u_0,\ldots,u_4]$，保普通单项式，并令

$$
D_5:E^{11}\otimes_E R_3\longrightarrow R_5,\qquad
(d_g)\longmapsto\sum_{g=0}^{10}q_gd_g.
$$

完整尺寸为

$$
\dim R_2=15,\quad\dim R_3=35,\quad\dim R_5=126,\qquad
D_5: E^{385}\longrightarrow E^{126}.
$$

原三次单位已经给 $qR_1=R_3$。乘遍 $R_2$ 得 $qR_3=R_5$，所以在原 $E$ 中

$$
\operatorname{rank}D_5=126,\qquad\dim_E\ker D_5=259.
\tag{2.1}
$$

程序还实际核其同原有限域矩阵秩126；这不是仅用行数假设满秩。

原385来源行按 $(g,m)$ 排列，$g=0,\ldots,10$、$m$ 为全部35个普通三次单项式。所有普通单项式按非降变量指标组合排序，不使用 divided-power 或对角额外系数。

令 $z_s\in E^{11}\otimes R_1$ 为已付二十条原低来源，$s=0,\ldots,19$。构造：

$$
K_5=
\bigl[u_\ell(q_a e_b-q_b e_a)\bigr]_
 {0\le\ell<5,\ 0\le a<b<11}
 \in E^{385\times275},
\tag{2.2}
$$

$$
H_5=
\bigl[m z_s\bigr]_
 {m\in\operatorname{Mon}_2(u),\ 0\le s<20}
 \in E^{385\times300}.
\tag{2.3}
$$

(2.3)保全部十五个普通二次乘子与全部二十条低来源，不只保留四路径的80列。

## 3. 原特征零身份与合法有限域门

原多项式交换性直接给

$$
D_5\bigl(u_\ell(q_a e_b-q_b e_a)\bigr)=0.
$$

原 $z_s$ 的完整三次核身份给

$$
D_5(mz_s)=m\sum_gq_gz_{g,s}=0.
$$

因此 $D_5K_5=D_5H_5=0$ 是原 $E$ 身份；不从有限域零乘积推上去。

实际程序逐完整原行核：

| 门 | 坐标数 |
|---|---:|
| $D_5K_5=0$ | 34650 |
| $D_5H_5=0$，全部300列 | 37800 |

随后对完整 $385\times275$ 原 $K_5$ 求秩。若秩小于259，则只登记 completed-diagnostic，exactEQuinticKoszulSpanProved 为 false；不从一次剩余域秩降低推出原 $E$ 秩降低。

若实际秩259，选择原259列及原259行，得到同原子式 $A$。必须实际核非零行列式和全部

$$
A A^{-1}=A^{-1}A=I_{259}.
$$

此实际原子式在合法 place 非零，因此在原 $E$ 非零。结合(2.1)和原 $D_5K_5=0$，严格得到

$$
\operatorname{im}_E K_5=\ker_E D_5.
\tag{3.1}
$$

原 $E$ 系数由这个原子式的伴随公式定义，不把有限域坐标搬成 $E$ 系数。

## 4. 实际满秩后的完整坐标证书

设原选中列为 $J$、原选中行为 $I$。程序实际计算

$$
C_K=\overline A^{-1}(\overline K_5)_I,\qquad
C_H=\overline A^{-1}(\overline H_5)_I.
$$

全部门包括：

| 完整门 | 坐标数 |
|---|---:|
| 两侧259阶单位逆 | 134162 |
| $(\overline K_5)_J C_K=\overline K_5$，全部275列 | 105875 |
| $(\overline K_5)_J C_H=\overline H_5$，全部300列 | 115500 |
| 全部16条原关系的 $K_5$ 乘回 | 6160 |
| 选中259列的坐标为单位矩阵 | 67081 |

原275列在满秩分支的核维数是16；程序用全部自由列构造完整关系，其自由坐标为单位矩阵，且逐385行乘回。这与 $\ker D_5/\operatorname{im}K_5$ 的维数为0是不同对象，不得混淆。

以上都是场上的完整原来源坐标证书；本次不求原 $E$ 大系数坐标数组，也不求参数大矩阵。

## 5. 全部二次低来源作用的真来源降次

以下只在(3.1)实际门成立后适用。

原 $C_s$ 有完整十一 $G$ 来源 $\sigma_s$，其 $u$ 次数至多一、线性最高部为 $z_s$。边界恒等式给

$$
\sigma(N_i v)=u_i\sigma(v)-\Sigma_i v.
\tag{5.1}
$$

所以每一个有序 $N_pN_qC_s$ 有真实原来源，$u$ 次数至多三，三次最高部为 $u_pu_qz_s$。其像仍属于十个保留单项式，普通 $u$ 次数至多二，故该最高来源确在 $B\otimes_E\ker D_5$，其中 $B=E[y,w]$。

由(3.1)，它可用(2.2)展开。使用同系数减去真正的完整来源

$$
u_\ell(G_a e_b-G_b e_a),
\tag{5.2}
$$

其原像严格为零，且最高部为对应 $u_\ell(q_a e_b-q_b e_a)$。减后来源次数至多二。

再用[实际混合95原选择](../results/R150-appendix-actual-original-koszul-fiftyfive-mixed95-unit-and-forty-source-selection.md)：先用已选40条真实 $N_iC_s$ 来源及真正 $G$-Koszul 消掉二次最高部，余次数至多一，由 exact-low20 的 canonical-source 唯一性降回原 $B C_{20}$。全过程只除固定 $E$ 常数，不倒参数。

因此全部有序二字都满足

$$
N_pN_qC_s\in
\mathcal C:=B\langle C_{20},W_{40}\rangle,
\tag{5.3}
$$

其中 $W_{40}$ 正是实际混合95选择的原列。程序核全部300个对称普通最高来源；有序算子两种次序具有同一最高部，而上述完整来源降次适用于每个有序来源，未假定自由十轴上的 $N_i$ 已交换。

## 6. 60列交换子模稳定及120／130上界

已付混合95定理给全部 $N_iC_s\in\mathcal C$。再由(5.3)，每条已选 $W=N_\ell C_s$ 的一次作用 $N_iW$ 也在 $\mathcal C$。$N_i$ 对 $B$ 线性，因此

$$
N_i\mathcal C\subset\mathcal C\qquad(0\le i<5).
\tag{6.1}
$$

这只断言60列交换子模稳定，不直接断言加入六 mean 后的第一轮稳定。

原全部高、低交换子都在 $\mathcal C$，所以五个 $N_i$ 在 $F/\mathcal C$ 上交换。原十一二次方程的字面 $e_0$ 关系和九条原路径保留，给出互逆的循环映射

$$
F/\mathcal C\simeq B[u]/(G_0,\ldots,G_{10}).
\tag{6.2}
$$

正向由原单项式行给出，因为每条 $\mathcal C$ 列都有真 $G$ 来源；反向由 $1\mapsto e_0$ 和取商后可交换的 $N_i$ 给出。字面路径保证两个复合分别固定十轴和循环元。这里不假设该商对 $B$ 自由。

六条原 mean 方程在(6.2)中由 $Y_1,\ldots,Y_6$ 表示。十个正常单项式

$$
1,\quad u_0,\ldots,u_4,\quad u_1u_4,u_2u_3,u_2u_4,u_3u_4
$$

已生成整个商作为 $B$ 模，因此 mean 理想只需这十个字面词作用于六条 $Y$，共至多60列。加交换子模的60列后：

$$
\boxed{\text{原十七梯度呈示至多120列；再加十条 Bell 列至多130列。}}
\tag{6.3}
$$

权分布为 $6$ 条权5、$20$ 条权6、$30$ 条权7、$40$ 条权8、$24$ 条权9；新增 Bell 是原 $(b-1)e_a$。不宣称这些生成元独立、最少、商自由或单位理想。

## 7. 父文件与同一新作业

本次读取已完整结束的两个父对象：

- high95 的全部原输入相位与 complete-unit 相位，binding 为 9f0ee10f7e4cece784d8140d063f94c210105e7dded9f811710d6ec6f2825fa1；
- actual mixed95 相位，binding 为 b0d3f4b6dfefddccd68f804561d74188c109c151329ac525e2f7b0d2e90a6232。

全部物理／逻辑相位和两个 manifest 都严 pin。新 consumer 还要求 mixed95 的原40索引为0至33、40至44和60，实际单位余数69，原95行等于 high95 所选行。原父算术不重标成新算术。

父作业已经关闭。新 job 真实顺序重建：

1. 原116 field model：180秒 / 2048 MiB，outer240；
2. 原 high95：60秒 / 512 MiB，outer120；
3. 原 mixed95：60秒 / 512 MiB，outer120；
4. 本次 quintic gate：60秒 / 512 MiB，outer120。

仅需已锁小源码；不恢复 exact 六逆、不再求旧Q60或two-four，不上传数组。完整父 CLI 与 support pins 在 inputs 中给出。

## 8. 冻结文件、CLI与预算

| 文件 | Git blob | 字节数 | SHA256 |
|---|---|---:|---|
| source | 17dc94b23638b15672461fa47206688caad3374f | 17017 | 5242360ddf86729c271ea55559c5a84870b7fb92ef73cc653f0cf6f64165d48c |
| inputs | de2b7b0c5fb0e873b116b108182b97f0e750ad4e | 12321 | 8b320e59d2154adb051d22105db38637afd948931c5842c6ac38186ebb80b7cb |

~~~text
notes/2026-11-16-r150-original-quintic-koszul-span259-unit127-789f.py
notes/2026-11-16-r150-original-quintic-koszul-span259-unit-inputs-789f.json
~~~

固定 Python3.12.14、python-flint0.9.0，不需 Singular。

~~~text
python 2026-11-16-r150-original-quintic-koszul-span259-unit127-789f.py \
  --high95-source {scripts}/2026-11-16-r150-original-quartic-syzygy95-small-field-gate127-789f.py \
  --high95-out {work}/original-quartic-syzygy95-small-gate127 \
  --mixed95-source {scripts}/2026-11-16-r150-original-koszul55-mixed95-source-unit127-789f.py \
  --mixed95-out {work}/original-koszul55-mixed95-unit127 \
  --out {work}/original-quintic-koszul259-unit127 \
  --seconds 60 \
  --memory-mib 512
~~~

沿用冻结 observer 的10秒心跳。原两侧来源和所有300 RHS均在同一版本、同一 binding 下核验。

## 9. 完整相位与失败范围

输入相位为 whole-original-quintic259-input.json.gz，完整满秩相位为 complete-original-quintic259-unit.json.gz。分别仅在其全部硬门通过后原子登记。manifest 与 receipt 名称为：

~~~text
original-quintic-koszul259-manifest.json
original-quintic-koszul259-receipt.json
~~~

fresh out 没有未实现的算术续接；75只代表真实预算和已登记完整相位，不能空重试或当作否定。错误的真实类型/message 放 parameters.error，最终保实际时长、峰值RSS、退出码和完整相位。

数学数组、全部坐标、raw和检查点只留临时目录或完成job日志；Git仅保存源码、参数、证明、执行身份及SHA。实际得到259之前，本接口§5—6严格保持条件式。
