# R133：完整moving多项式实现与实际全列核验
+
+**有限浮点实现与数值证据，非连续PDE证书。** 数学系统使用已证的完整moving曲率角等价，边界使用已证的完整物理矩公式；状态标识明确写为moving phi，不把旧physical theta的PPoly数组重新解释成新状态。
+
+## 全部内部项
+
+设u=αU、v=s+αV、m=s+αV0、S=α²U²+Kv²、d=−βI(S)。实际未投影的两行是
+
+$$U_r=dU_φ+γmK V_φ−βU(1+α²U²+Kv²),$$
+$$V_r=dV_φ−γm U_φ+β[V−K(3s²V+3αsV²+α²V³)−αvU²].$$
+
+有限M输入时S与d完整到2M，右端完整到3M。Jacobian的非局部列准确为
+δd=−βI(2α²UδU+2αKvδV)，必须先保留全部2M再与Uφ/Vφ相乘；源码使用完整矩形Toeplitz/Hankel乘法。另有完整V0列αγ(KVφ,−Uφ)。ν列保留ds/dν、dK/dν、dγ/dν及对应d的变化。
+
+独立full_action直接用完整FFT与primitive计算，不重用已装配矩阵。普通批处理只拆独立径向列。新边界直接计算所有保留的physical B/C矩、全部状态列、mean和ν列；Cmean=1/m准确使用，不用角梯形重算mean。N>6M只说明内部三次去混叠，不能说明指数边界积分或全部变角尾已经严格支付。
+
+## 已实际运行的必要检查
+
+原真实目标、完整primitive、真实q向量上，M7/N64、六个实际半径、所有15状态列和ν列都经过检查。结果：
+
+- 完整FFT action与全Jacobian最大差：1.13686837721616e-13。
+- 非线性全部内列中心差分最大差：1.453454339522819e-09。
+- 真mean方程反馈恒等式误差：5.329070518200751e-15。
+- 所有边界状态及ν列中心差分最大差：5.04257746669623e-10。
+- 用独立16384点uniform physical角逆图重算物理矩，全部保留系数最大差：5.757113535898029e-16。
+
+准确3M支持外仅舍入量，六门全部通过，实际用时约1.57秒。中心差分和双角网用于实现风险检查，未冒充有向无限维证书。
+
+源为 `scripts/fourfold_codazzi_moving_polynomial_system.py` 和 `scripts/fourfold_codazzi_moving_operator_audit.py`；原报告 `notes/2026-11-13-R133-moving-complete-small-operator-audit.json` 保留源/对象/q SHA、完整字段、原门及全部实际结果。下一步实际求新有限系统并检完整残差、真帽及全频逆；原M256物理坐标求解同时按完整检查点继续。
+