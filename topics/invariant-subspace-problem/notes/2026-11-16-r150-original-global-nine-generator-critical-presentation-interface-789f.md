# 原全局九生成元临界表示：执行与消费接口

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16。

~~~sh
python 2026-11-16-r150-original-global-nine-generator-critical-presentation-789f.py \
  --presentation-out PRESENTATION_OUT --six-out SIX_OUT \
  --chart-helper 2026-11-16-r150-original-complete-fifty-six-seven-generator-charts-v2-789f.py \
  --out OUT --seconds 180 --memory-mib 768
~~~

依赖 Python 3.12 和 python-flint 0.9.0。原输入、源码和 helper 的完整 pins 见同目录 inputs。
实际运行已 exit0，12.36292547499761 秒，最大常驻112848 KiB；其中固定常矩阵 Dixon 为7.0993933040008415秒。

## 1. 原固定常数单位

读取原四个 $T_i$ 中的 $T_1$，全部36个条目在同一原三次域 $E$ 中。
18×18有理正则表示的324个坐标均由原 $T_1$ 重建。
仅求6个右端，完整候选先保存，再通过整数行列清分母核全部108个原有理产品，
并直接核全部36个 $E$ 左逆产品。只有此后才写 verified inverse。

完整inverse文件是本次新原常数叶，编号等于母算术图 originalInputFiles 的长度。
后继必须将 arithmetic extension 的 appendedOriginalInputFiles 接在母列表后解析，
不能将新增叶误读成另一个目录的第0号文件。

## 2. 实际原关系与消去

母68列只取0…49和61…67共57列。母基第6行是 $v_1=u_1u_4$，
其余原行按 $[0,1,2,3,4,5,7,8,9]$ 保留。

令 $\eta=w^{\mathsf T}T_1^{-1}$，$r=\sum_j\eta_jh_j$。
原二次块给 $r_6=b=y\cdot w$。
原零来源 literal 边界列精确满足
$$
R_{1,u_4}+u_1R_{4,0}=u_1u_4e_0-e_6.
$$
因此
$$
r_h=r+(b-1)(R_{1,u_4}+u_1R_{4,0})-u_1u_4R_{\rm Bell}
=r-(b-1)e_6
$$
是原57列的明确组合，且第6坐标严格为1。没有补全任何6阶可逆参数矩阵。

对每个原列 $p$，完整9向量为
$$
p'_K=p_K-(r_h)_Kp_6.
$$
若原18来源为 $s_p$，则新来源准确为
$$
s'_p=s_p-p_6s_{r_h},\qquad
s_{r_h}=\sum_j\eta_js_{h_j}-u_1u_4e_{\rm Bell}.
$$
全部57列、全部1026原源坐标都保存；没有只存独立抽样列。

## 3. 输出图语义与准确范围

完成文件：complete-original-global-nine-critical-presentation.json.gz。
扩展图：complete-original-global-nine-arithmetic-extension.json.gz。
原常数候选和 verified inverse 分别单独封存。

105774个母节点保持原编号。本次只追加2889节点，原parameter polynomial仍按母图叶解析。
所有新节点无前向引用；固定 $E$ 逆只是常数叶，图中没有参数逆。
literalUnitRelationOriginal68ColumnCombination 给真正的原列组合；
其中11个已删 moment-gradient 位置仍为零。

矩阵为9×57，所有条目对 $u$ 至多一次。
原source含 Bell−1 来源 $-u_1u_4$，故最大 $u$ 次数实际为3；不可将矩阵的一次上界移给来源。
母原source身份与本次精确常逆、通用行列代入共同给全参数证明；
没有宣称将所有巨大参数乘积重新完全展开。

在 $E[y,w]/(b-1)[u]$ 上，末Bell列确为零，去掉它得9×56。
该表示与原完整 Bell 归一临界商同构，不是自由九模或判空结论。
数据没有加入rank4、参数一般位置或任何特定实嵌入假设。
