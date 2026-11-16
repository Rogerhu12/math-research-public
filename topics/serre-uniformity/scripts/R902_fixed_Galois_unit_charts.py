#!/usr/bin/env python3
"""Fixed original unit charts for the R902 constant-field Galois consumer.
This module is imported only by the public Actions mathematical driver.
It never selects a new pivot, free column, projection row or section.
"""
import gc
from flint import nmod_mat

P=1000000753

class FixedChartNonunit(RuntimeError):
    pass

def mat(raw):
    return nmod_mat(raw,P)

def rows(M):
    return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]

def sub(M,I,J):
    return mat([[int(M[i,j]) for j in J] for i in I])

def zero(m,n):
    return nmod_mat(m,n,P)

def eye(n):
    return mat([[int(i==j) for j in range(n)] for i in range(n)])

def joined(A,B):
    assert A.nrows()==B.nrows()
    return mat([[int(A[i,j]) for j in range(A.ncols())]+
                [int(B[i,j]) for j in range(B.ncols())] for i in range(A.nrows())])

def matrix_shape(raw,m,n):
    assert len(raw)==m and all(len(row)==n for row in raw)

def chart_template(source_reference,source_old_minor,rows_selected,columns_selected,
                   free_columns,full_shape,rank,old_exact_definition):
    """An IO description of an already completed original chart, never a new selection."""
    m,n=full_shape
    assert len(rows_selected)==len(columns_selected)==rank
    assert rows_selected==sorted(set(rows_selected))
    assert columns_selected==sorted(set(columns_selected))
    assert free_columns==sorted(set(free_columns))
    assert sorted(columns_selected+free_columns)==list(range(n))
    assert all(0<=i<m for i in rows_selected)
    return {
        "source_original_complete_kernel":source_reference,
        "source_original_selected_unit_minor":source_old_minor,
        "source_original_exact_definition":old_exact_definition,
        "matrix_shape":[m,n],"rank":rank,
        "selected_rows":rows_selected,"pivot_columns":columns_selected,
        "free_columns":free_columns,
        "selection_is_inherited_from_original_sigma0":True,
        "new_selection_or_rescaling_allowed":False,
    }

def solve_fixed_two_rhs(job,stem,square,rhs,template,free_weights,
                        source_selected_rows,exact_definition):
    """Solve only the two inherited free-coordinate vectors of the initial chart.

    rhs is +S[I,F]*free_weights.  The original chart and exact conjugation define
    all nullity columns, but only these two columns are physically formed here.
    Full original A-yB checks are mandatory in the calling driver.
    """
    rank=template["rank"];m,n=template["matrix_shape"]
    I=template["selected_rows"];J=template["pivot_columns"];F=template["free_columns"]
    assert square.nrows()==square.ncols()==rank
    assert rhs.nrows()==rank and rhs.ncols()==2
    assert free_weights.nrows()==len(F) and free_weights.ncols()==2
    assert template["selection_is_inherited_from_original_sigma0"] is True
    assert template["new_selection_or_rescaling_allowed"] is False
    assert len(I)==len(J)==rank and len(F)==n-rank
    assert sorted(J+F)==list(range(n))
    name=stem+"-fixed-original-unit-minor"
    minor=job.old(name)
    if minor is None:
        job.budget();determinant=int(square.det())
        minor=job.put(name,{
            "prime":P,"source_original_chart":template,
            "source_new_selected_rows":source_selected_rows,
            "matrix_shape":[rank,rank],"selected_rows":I,"selected_columns":J,
            "actual_determinant_mod_prime":determinant,"actual_unit":determinant!=0,
            "original_rows_and_columns_preserved":True,"new_pivot_search_performed":False,
            "nonunit_does_not_disprove_original_characteristic_zero_conjugate":determinant==0,
        })
        job.checkpoint(name)
    assert minor["source_original_chart"]==template
    assert minor["source_new_selected_rows"]==source_selected_rows
    if not minor["actual_unit"]:
        raise FixedChartNonunit("The fixed original initial chart is not a unit: "+stem)
    assert minor["actual_determinant_mod_prime"]!=0
    rawname=stem+"-two-inherited-free-RHS"
    raw=job.old(rawname)
    if raw is None:
        job.budget();augmented=joined(square,rhs)
        reduced,actual_rank=augmented.rref()
        assert actual_rank==rank
        assert sub(reduced,list(range(rank)),list(range(rank)))==eye(rank)
        solution=-sub(reduced,list(range(rank)),[rank,rank+1])
        assert square*solution+rhs==zero(rank,2)
        values=[[0,0] for _ in range(n)]
        for i,original in enumerate(F):
            values[original]=[int(free_weights[i,k]) for k in range(2)]
        for i,original in enumerate(J):
            values[original]=[int(solution[i,k]) for k in range(2)]
        B=mat(values)
        assert sub(B,F,[0,1])==free_weights
        raw=job.put(rawname,{
            "prime":P,"source_original_chart":template,
            "source_actual_conjugate_unit_minor":job.ref(name),
            "source_new_selected_rows":source_selected_rows,
            "matrix_shape":[n,2],"B_coefficients_mod_prime":values,
            "fixed_free_weights_mod_prime":rows(free_weights),
            "selected_rows":I,"pivot_columns":J,"free_columns":F,
            "fixed_free_coordinates_verified":True,
            "all_selected_original_rows_times_two_columns_zero":True,
            "complete_initial_space_exact_unit_solve_defined":True,
            "exact_complete_space_definition":{
                "source_original_chart":template,
                "conjugate_exact_definition":exact_definition,
                "all_pivot_columns_formula":"-sigma(S[I,J])^-1*sigma(S[I,F])",
                "all_free_columns_formula":"the original identity",
                "original_char0_rank_preserved_by_true_constant_field_conjugation":True,
            },
            "exact_two_columns_definition":{
                "conjugate_exact_definition":exact_definition,
                "pivot_formula":"-sigma(S[I,J])^-1*sigma(S[I,F])*original_integer_weights",
                "free_formula":"original_integer_weights",
                "original_integer_weights_fixed_by_constant_field_Galois":True,
            },
            "materialized_initial_B_columns":2,
            "full_conjugate_initial_B_basis_numerically_materialized":False,
            "full_square_inverse_materialized":False,
            "all_unselected_original_fibre_relations_yet_verified_here":False,
            "characteristic_zero_coefficients_expanded":False,
        })
        job.checkpoint(rawname)
        del augmented,reduced,solution,B;gc.collect()
    assert raw["source_original_chart"]==template
    assert raw["source_actual_conjugate_unit_minor"]==job.ref(name)
    assert raw["source_new_selected_rows"]==source_selected_rows
    assert raw["fixed_free_weights_mod_prime"]==rows(free_weights)
    matrix_shape(raw["B_coefficients_mod_prime"],n,2)
    return mat(raw["B_coefficients_mod_prime"]),raw,job.ref(rawname)

def solve_fixed_unit_kernel(job,stem,M,template,exact_definition,row_block_size=272):
    """Return the unique conjugated canonical kernel with the original free identity.

    job supplies budget/old/put/ref/checkpoint and its own source-bound tag.
    All source references in template point to the actual sigma0 producer.
    """
    m,n=M.nrows(),M.ncols()
    assert template["matrix_shape"]==[m,n]
    assert template["selection_is_inherited_from_original_sigma0"] is True
    assert template["new_selection_or_rescaling_allowed"] is False
    I=template["selected_rows"];J=template["pivot_columns"];F=template["free_columns"]
    rank=template["rank"];nullity=n-rank
    assert len(I)==len(J)==rank and len(F)==nullity
    assert sorted(J+F)==list(range(n))
    assert row_block_size>0
    name=stem+"-fixed-original-unit-minor"
    minor=job.old(name)
    if minor is None:
        job.budget()
        square=sub(M,I,J)
        determinant=int(square.det())
        minor=job.put(name,{
            "prime":P,"source_original_chart":template,
            "matrix_shape":[rank,rank],
            "selected_rows":I,"selected_columns":J,
            "actual_determinant_mod_prime":determinant,
            "actual_unit":determinant!=0,
            "original_rows_and_columns_preserved":True,
            "nonunit_does_not_disprove_original_characteristic_zero_conjugate":determinant==0,
            "new_pivot_search_performed":False,
        })
        job.checkpoint(name)
        del square;gc.collect()
    assert minor["source_original_chart"]==template
    if not minor["actual_unit"]:
        raise FixedChartNonunit("The fixed original chart is not a unit at this conjugate: "+stem)
    assert minor["actual_determinant_mod_prime"]!=0

    rawname=stem+"-fixed-free-identity-kernel"
    raw=job.old(rawname)
    if raw is None:
        job.budget()
        square=sub(M,I,J);rhs=sub(M,I,F)
        augmented=joined(square,rhs)
        reduced,actual_rank=augmented.rref()
        assert actual_rank==rank
        assert sub(reduced,list(range(rank)),list(range(rank)))==eye(rank)
        solution=-sub(reduced,list(range(rank)),list(range(rank,rank+nullity)))
        assert square*solution+rhs==zero(rank,nullity)
        values=[[0]*nullity for _ in range(n)]
        for j,original in enumerate(F):
            values[original][j]=1
        for i,original in enumerate(J):
            values[original]=[int(solution[i,j]) for j in range(nullity)]
        K=mat(values)
        assert sub(K,F,list(range(nullity)))==eye(nullity)
        assert sub(M,I,list(range(n)))*K==zero(rank,nullity)
        raw=job.put(rawname,{
            "prime":P,"source_original_chart":template,
            "source_actual_conjugate_unit_minor":job.ref(name),
            "matrix_shape":[n,nullity],
            "selected_rows":I,"pivot_columns":J,"free_columns":F,
            "kernel_basis_mod_prime":values,
            "fixed_free_identity_verified":True,
            "all_selected_original_rows_times_kernel_zero":True,
            "all_selected_pivot_RHS_multiplied_back":True,
            "full_square_inverse_materialized":False,
            "actual_solve":"rref([M[I,J],M[I,F]]) with the fixed first rank columns already certified units",
            "exact_unit_solve_expression":{
                "source_original_chart":template,
                "conjugate_exact_definition":exact_definition,
                "pivot_formula":"-sigma(M[I,J])^-1*sigma(M[I,F])",
                "free_formula":"the same original identity",
                "old_selected_rows_free_order_and_integer_parameters_preserved":True,
            },
            "full_unselected_rows_yet_certified_here":False,
            "characteristic_zero_coefficients_expanded":False,
        })
        job.checkpoint(rawname)
        del square,rhs,augmented,reduced,solution,K;gc.collect()
    assert raw["source_original_chart"]==template
    assert raw["source_actual_conjugate_unit_minor"]==job.ref(name)
    matrix_shape(raw["kernel_basis_mod_prime"],n,nullity)
    K=mat(raw["kernel_basis_mod_prime"])
    checks=[]
    for first in range(0,m,row_block_size):
        stop=min(first+row_block_size,m)
        checkname=stem+f"-all-original-rows-{first:06d}-{stop:06d}"
        check=job.old(checkname)
        if check is None:
            job.budget()
            assert sub(M,list(range(first,stop)),list(range(n)))*K==zero(stop-first,nullity)
            check=job.put(checkname,{
                "prime":P,"source_actual_conjugate_kernel":job.ref(rawname),
                "original_row_interval":[first,stop],"checked_shape":[stop-first,nullity],
                "all_original_rows_in_interval_times_kernel_zero":True,
                "source_original_chart":template,
            })
            job.checkpoint(checkname)
        assert check["source_actual_conjugate_kernel"]==job.ref(rawname)
        assert check["original_row_interval"]==[first,stop]
        checks.append(job.ref(checkname))
    finalname=stem+"-complete-fixed-original-kernel"
    certificate=job.old(finalname)
    if certificate is None:
        certificate=job.put(finalname,{
            "prime":P,"matrix_shape":[m,n],
            "actual_rank":rank,"actual_complete_kernel_dimension":nullity,
            "source_original_chart":template,
            "source_actual_conjugate_unit_minor":job.ref(name),
            "source_actual_conjugate_kernel":job.ref(rawname),
            "source_all_original_row_checks":checks,
            "all_original_rows_checked":m,
            "all_original_rows_times_kernel_zero":True,
            "fixed_free_identity_verified":True,
            "complete_conjugate_characteristic_zero_space_certified":True,
            "exact_conjugate_definition":exact_definition,
            "proof":"original characteristic-zero conjugation preserves rank; fixed unit minor and full-row multiplication certify this residue image",
            "old_sigma0_matrix_or_kernel_recomputed":False,
            "new_rows_columns_free_order_or_anchor_chosen":False,
            "characteristic_zero_coefficients_expanded":False,
        })
        job.checkpoint(finalname)
    assert certificate["source_original_chart"]==template
    assert certificate["source_all_original_row_checks"]==checks
    return K,certificate,job.ref(finalname)

def fixed_second_projection(job,name,K,kernel_ref,source_original_projection,
                            original_independent_rows,dimension,exact_definition):
    """Second690 projection with the actual original independence rows, not a new RREF."""
    assert K.nrows()==1380 and K.ncols()==dimension
    I=original_independent_rows
    assert len(I)==dimension and I==sorted(set(I)) and all(0<=i<690 for i in I)
    value=job.old(name)
    if value is None:
        job.budget()
        projected=sub(K,list(range(690,1380)),list(range(dimension)))
        determinant=int(sub(projected,I,list(range(dimension))).det())
        if determinant==0:
            failname=name+"-fixed-unit-failure"
            job.put(failname,{
                "prime":P,"source_actual_conjugate_kernel":kernel_ref,
                "source_original_projection":source_original_projection,
                "original_independent_normal_rows":I,
                "actual_selected_determinant_mod_prime":0,
                "new_projection_rows_chosen":False,
                "conjugate_characteristic_zero_projection_disproved":False,
            })
            job.checkpoint(failname)
            raise FixedChartNonunit("The inherited projection chart is nonunit: "+name)
        value=job.put(name,{
            "prime":P,"source_actual_conjugate_kernel":kernel_ref,
            "source_original_projection":source_original_projection,
            "projection_rows":[690,1380],
            "normal_V3_basis":[list(p) for p in job.V3],
            "matrix_shape":[690,dimension],
            "normal_V3_basis_mod_prime":rows(projected),
            "original_independent_normal_rows":I,
            "actual_projection_minor_determinant_mod_prime":determinant,
            "complete_conjugate_RR_space_certified":True,
            "exact_conjugate_space":exact_definition,
            "new_projection_rows_chosen":False,
            "normal_integer_scale_applied_again":False,
            "characteristic_zero_coefficients_expanded":False,
        })
        job.checkpoint(name)
    assert value["source_actual_conjugate_kernel"]==kernel_ref
    assert value["source_original_projection"]==source_original_projection
    assert value["original_independent_normal_rows"]==I
    matrix_shape(value["normal_V3_basis_mod_prime"],690,dimension)
    return mat(value["normal_V3_basis_mod_prime"]),value,job.ref(name)
